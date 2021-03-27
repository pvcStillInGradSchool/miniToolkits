#!/usr/bin/env python3
"""Define Scheduler."""

from graph import DirectedGraph
from graph import TopologicalSort
from graph import UnionFind


class Scheduler:
    """A scheduler supporting O(1) adding and O(N) scheduling."""

    def __init__(self):
        self._task_to_id = dict()
        self._id_to_task = list()
        self._graph = DirectedGraph()
        self._union = UnionFind()

    def add_a_task(self, task):
        """Add a new task.

        Do nothing, if the task has already been added.
        """
        if task not in self._task_to_id:
            i_task = self.n_tasks()
            self._task_to_id[task] = i_task
            self._id_to_task.append(task)
        assert len(self._id_to_task) == len(self._task_to_id)
        assert task == self._id_to_task[self._task_to_id[task]]

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
        self.add_a_task(task)
        self.add_a_task(prerequisite)
        i_task = self._task_to_id[task]
        i_prerequisite = self._task_to_id[prerequisite]
        self._graph.connect(i_task, i_prerequisite)
        self._union.connect(i_task, i_prerequisite)

    def add_prerequisites(self, task, prerequisites):
        """Add multiple prerequisites for a task."""
        for prerequisite in prerequisites:
            self.add_a_prerequisite(task, prerequisite)

    def schedule(self):
        """Return the tasks in topologically sorted order."""
        sorted_tasks = TopologicalSort(self._graph).sort()
        # Make immutable copies.
        scheduled_tasks = set()
        for a_component in self._to_components(sorted_tasks):
            scheduled_tasks.add(tuple(a_component))
        return scheduled_tasks

    def _to_components(self, sorted_tasks):
        root_to_component = dict()
        for i_task in sorted_tasks:
            i_root = self._union.root(i_task)
            if i_root not in root_to_component:
                root_to_component[i_root] = list()
            task = self._id_to_task[i_task]
            root_to_component[i_root].append(task)
        return root_to_component.values()

if __name__ == "__main__":
    import sys
    A_SCHEDULER = Scheduler()
    for line in sys.stdin:
        if line[0] != '#':
            task_and_prerequisites = line.split()
            A_SCHEDULER.add_prerequisites(
                task_and_prerequisites[0],
                task_and_prerequisites[1:]
            )
    i = 0
    for one_component_of_scheduled_tasks in A_SCHEDULER.schedule():
        i += 1
        print('Independent Task Group {0}:'.format(i))
        for a_task in one_component_of_scheduled_tasks:
            print('  ' + a_task)
