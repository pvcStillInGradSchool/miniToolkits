"""Define Scheduler."""

class Scheduler:
    """Schedule a set of tasks."""

    def __init__(self):
        self._task_to_prerequisites = dict()
        self._touched_tasks = set()
        self._finished_tasks = set()
        self._sorted_tasks = list()

    def add_a_task(self, task):
        """Add a new task.

        Do nothing, if the task has already been added.
        """
        if self._has_not_added(task):
            self._task_to_prerequisites[task] = set()

    def add_tasks(self, tasks):
        """Add multiple tasks."""
        for task in tasks:
            self.add_a_task(task)

    def count_tasks(self):
        """Return the number of tasks being added."""
        return len(self._task_to_prerequisites)

    def add_a_prerequisite(self, task, prerequisite):
        """Add a prerequisite for a task.

        Automatically add a new task, if any of the two is new.
        Do nothing, if the prerequisite has already been added.
        """
        if self._has_not_added(task):
            self.add_a_task(task)
        if self._has_not_added(prerequisite):
            self.add_a_task(prerequisite)
        self._task_to_prerequisites[task].add(prerequisite)

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
        return prerequisite in self._task_to_prerequisites[task]

    def schedule(self):
        """Return the tasks in topologically sorted order."""
        self._reset()
        for task in self._task_to_prerequisites:
            if self._has_not_touched(task):
                self._depth_first_search(task)
        self._assert_equal_length()
        task_to_root = dict()
        root_to_components = dict()
        for task in self._sorted_tasks:
            if self._has_no_prerequisite(task):
                task_to_root[task] = task
                root_to_components[task] = list()
            else:
                prerequisite = self._get_a_prerequisite(task)
                task_to_root[task] = task_to_root[prerequisite]
            component = root_to_components[task_to_root[task]]
            component.append(task)
        scheduled_tasks = set()
        for component in root_to_components.values():
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

    def _has_not_touched(self, task):
        return task not in self._touched_tasks

    def _has_not_finished(self, task):
        return task not in self._finished_tasks

    def _reset(self):
        self._touched_tasks.clear()
        self._finished_tasks.clear()
        self._sorted_tasks.clear()

    def _depth_first_search(self, task):
        self._touched_tasks.add(task)
        for prerequisite in self._task_to_prerequisites[task]:
            if self._has_not_finished(prerequisite):
                assert self._has_not_touched(prerequisite), 'Cycle detected!'
                self._depth_first_search(prerequisite)
        self._finished_tasks.add(task)
        self._sorted_tasks.append(task)

    def _assert_equal_length(self):
        assert (len(self._touched_tasks) == len(self._finished_tasks) ==
                len(self._sorted_tasks) == len(self._task_to_prerequisites))


if __name__ == "__main__":
    pass
