"""Define Scheduler."""

import graph


class Scheduler:
    """Schedule a set of tasks."""

    def __init__(self):
        self._task_to_prerequisites = dict()
        self._task_to_id = dict()
        self._id_to_task = list()
        self._union = graph.Union()
        # self._task_to_parent = dict()
        # self._task_to_size = dict()
        self._touched_tasks = set()
        self._finished_tasks = set()
        self._sorted_tasks = list()

    def add_a_task(self, task):
        """Add a new task.

        Do nothing, if the task has already been added.
        """
        if self._has_not_added(task):
            self._task_to_prerequisites[task] = set()
            self._task_to_id[task] = self.n_tasks()
            self._id_to_task.append(task)

    def add_tasks(self, tasks):
        """Add multiple tasks."""
        for task in tasks:
            self.add_a_task(task)

    def n_tasks(self):
        """Return the number of tasks being added."""
        return len(self._task_to_id)

    def add_a_prerequisite(self, task, prerequisite):
        """Add a prerequisite for a task.

        Automatically add a new task, if any of the two is new.
        Do nothing, if the prerequisite has already been added.
        """
        if self._has_not_added(task):
            self.add_a_task(task)
        if self._has_not_added(prerequisite):
            self.add_a_task(prerequisite)
        self._connect_tasks(task, prerequisite)

    def _connect_tasks(self, task_a, task_b):
        self._task_to_prerequisites[task_a].add(task_b)
        id_a = self._task_to_id[task_a]
        id_b = self._task_to_id[task_b]
        self._union.connect(id_a, id_b)

    def add_prerequisites(self, task, prerequisites):
        """Add multiple prerequisites for a task."""
        for prerequisite in prerequisites:
            self.add_a_prerequisite(task, prerequisite)

    def check_dependency(self, task, prerequisite):
        """Whether task depends on prerequisite?"""
        if self._has_not_added(task):
            return False
        if self._has_not_added(prerequisite):
            return False
        self._reset()
        self._depth_first_touch(task)
        return self._has_touched(prerequisite)

    def _depth_first_touch(self, task):
        """Touch-only Depth-First-Search."""
        self._touched_tasks.add(task)
        for prerequisite in self._task_to_prerequisites[task]:
            if self._has_not_touched(prerequisite):
                self._depth_first_touch(prerequisite)

    def schedule(self):
        """Return the tasks in topologically sorted order."""
        self._reset()
        for task in self._task_to_prerequisites:
            if self._has_not_touched(task):
                self._topo_sort(task)
        self._assert_equal_length()
        return self._pack_scheduled_tasks()

    def _pack_scheduled_tasks(self):
        root_to_component = dict()
        for task in self._sorted_tasks:
            root = self._union.root(self._task_to_id[task])
            if root not in root_to_component:
                root_to_component[root] = list()
            root_to_component[root].append(task)
        scheduled_tasks = set()
        for component in root_to_component.values():
            scheduled_tasks.add(tuple(component))
        return scheduled_tasks

    def _has_no_prerequisite(self, task):
        prerequisites = self._task_to_prerequisites[task]
        return len(prerequisites) == 0

    def _get_a_prerequisite(self, task):
        prerequisites = self._task_to_prerequisites[task]
        return next(iter(prerequisites))

    def _has_not_added(self, task):
        return task not in self._task_to_prerequisites

    def _has_touched(self, task):
        return task in self._touched_tasks

    def _has_not_touched(self, task):
        return task not in self._touched_tasks

    def _has_not_finished(self, task):
        return task not in self._finished_tasks

    def _reset(self):
        self._touched_tasks.clear()
        self._finished_tasks.clear()
        self._sorted_tasks.clear()

    def _topo_sort(self, task):
        """Topologically sort all the downstream tasks reachable from task."""
        self._touched_tasks.add(task)
        for prerequisite in self._task_to_prerequisites[task]:
            if self._has_not_finished(prerequisite):
                assert self._has_not_touched(prerequisite), 'Cycle detected!'
                self._topo_sort(prerequisite)
        self._finished_tasks.add(task)
        self._sorted_tasks.append(task)

    def _assert_equal_length(self):
        assert (len(self._touched_tasks) == len(self._finished_tasks) ==
                len(self._sorted_tasks) == len(self._task_to_prerequisites))


if __name__ == "__main__":
    import sys
    a_scheduler = Scheduler()
    for line in sys.stdin:
        if line[0] != '#':
            tasks = line.split()
            a_scheduler.add_prerequisites(tasks[0], tasks[1:])
    i = 0
    for component in a_scheduler.schedule():
        i += 1
        print('Independent Task Group {0}:'.format(i))
        for task in component:
            print('  ' + task)
