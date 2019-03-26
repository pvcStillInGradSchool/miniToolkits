"""Define Scheduler."""

class Scheduler:
    """Schedule a set of tasks."""

    def __init__(self):
        pass

    def add_task(self, task):
        """Add a new task.

        Do nothing, if the task has already been added.
        """

    def count_tasks(self):
        """Return the number of tasks being added."""

    def add_dependency(self, task, prerequisite):
        """Add a new dependency."""

    def count_dependencies(self):
        """Return the number of dependencies being added."""

    def schedule(self):
        """Schedule added tasks being added."""


if __name__ == "__main__":
    pass
