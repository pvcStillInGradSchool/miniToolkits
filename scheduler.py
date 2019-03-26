"""Define Scheduler."""

class Scheduler:
    """Schedule a set of tasks."""

    def __init__(self):
        self._task_to_dependencies = dict()

    def add_a_task(self, task):
        """Add a new task.

        Do nothing, if the task has already been added.
        """
        if self._is_new(task):
            self._task_to_dependencies[task] = set()

    def _is_new(self, task):
        return task not in self._task_to_dependencies

    def count_tasks(self):
        """Return the number of tasks being added."""
        return len(self._task_to_dependencies)

    def add_a_dependency(self, task, dependency):
        """Add a new dependency.

        Automatically add a new task, if any of the two is new.
        Do nothing, if the dependency has already been added.
        """
        if self._is_new(task):
            self.add_a_task(task)
        if self._is_new(dependency):
            self.add_a_task(dependency)
        self._task_to_dependencies[task].add(dependency)

    def count_dependencies(self):
        """Return the number of dependencies being added."""

    def schedule(self):
        """Schedule added tasks being added."""


if __name__ == "__main__":
    pass
