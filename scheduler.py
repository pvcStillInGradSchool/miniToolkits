"""Define Scheduler."""

class Scheduler:
    """Schedule a set of tasks."""

    def __init__(self):
        self._task_to_dependencies = dict()
        self._touched_tasks = set()
        self._finished_tasks = set()
        self._sorted_tasks = list()

    def add_a_task(self, task):
        """Add a new task.

        Do nothing, if the task has already been added.
        """
        if self._has_not_added(task):
            self._task_to_dependencies[task] = set()

    def count_tasks(self):
        """Return the number of tasks being added."""
        return len(self._task_to_dependencies)

    def add_a_dependency(self, task, dependency):
        """Add a new dependency.

        Automatically add a new task, if any of the two is new.
        Do nothing, if the dependency has already been added.
        """
        if self._has_not_added(task):
            self.add_a_task(task)
        if self._has_not_added(dependency):
            self.add_a_task(dependency)
        self._task_to_dependencies[task].add(dependency)

    def check_dependency(self, task, dependency):
        """Whether task depends on dependency?"""
        if self._has_not_added(task):
            return False
        if self._has_not_added(dependency):
            return False
        return dependency in self._task_to_dependencies[task]

    def schedule(self):
        """Return the tasks in topologically sorted order."""
        self._reset()
        for task in self._task_to_dependencies:
            if self._has_not_touched(task):
                self._depth_first_search(task)
        self._assert_equal_length()
        return self._sorted_tasks

    def _has_not_added(self, task):
        return task not in self._task_to_dependencies

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
        for depended_task in self._task_to_dependencies[task]:
            if self._has_not_finished(depended_task):
                assert self._has_not_touched(depended_task), 'Cycle detected!'
                self._depth_first_search(depended_task)
        self._finished_tasks.add(task)
        self._sorted_tasks.append(task)

    def _assert_equal_length(self):
        assert (len(self._touched_tasks) == len(self._finished_tasks) ==
                len(self._sorted_tasks) == len(self._task_to_dependencies))


if __name__ == "__main__":
    pass
