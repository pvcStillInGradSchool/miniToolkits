"""Test Scheduler."""

import unittest

from scheduler import Scheduler


class TestScheduler(unittest.TestCase):
    """Test the correctness of scheduler.Scheduler."""

    def test_empty_task_set(self):
        """Test public methods on an empty task set."""
        a_scheduler = Scheduler()
        self.assertEqual(a_scheduler.n_tasks(), 0)
        schedued_tasks = a_scheduler.schedule()
        self.assertEqual(schedued_tasks, set())

    def test_linked_list(self):
        """Test public methods on a task set, which forms a linked list."""
        a_scheduler = Scheduler()
        self.assertEqual(a_scheduler.n_tasks(), 0)
        a_scheduler.add_a_task('A')
        self.assertEqual(a_scheduler.n_tasks(), 1)
        a_scheduler.add_a_task('B')
        self.assertEqual(a_scheduler.n_tasks(), 2)
        a_scheduler.add_a_task('B')
        self.assertEqual(a_scheduler.n_tasks(), 2)
        a_scheduler.add_tasks(('C', 'D'))
        self.assertEqual(a_scheduler.n_tasks(), 4)
        # Build the dependency graph, which is a linked list:
        #   A <- B <- C <- D
        a_scheduler.add_a_prerequisite(task='B', prerequisite='A')
        a_scheduler.add_a_prerequisite(task='C', prerequisite='B')
        a_scheduler.add_a_prerequisite(task='D', prerequisite='C')
        # Only one result is correct.
        schedued_tasks = a_scheduler.schedule()
        self.assertEqual(schedued_tasks, {('A', 'B', 'C', 'D')})

    def test_binary_tree(self):
        """Test public methods on a task set, which forms a binary tree."""
        a_scheduler = Scheduler()
        # Build the dependency graph, which is a binary tree:
        #     A
        #    / \
        #   B   C
        a_scheduler.add_a_prerequisite(task='B', prerequisite='A')
        a_scheduler.add_a_prerequisite(task='C', prerequisite='A')
        # Two possible results:
        #   - A must appears before B and C.
        #   - No requirements on the relative order of B and C.
        schedued_tasks = a_scheduler.schedule()
        self.assertTrue(schedued_tasks in (
            {('A', 'B', 'C')},
            {('A', 'C', 'B')}
        ))

    def test_reversed_binary_tree(self):
        """Test public methods on a task set, which forms a reversed binary tree."""
        a_scheduler = Scheduler()
        # Build the dependency graph, which is a reversed binary tree:
        #   B   C
        #    \ /
        #     A
        a_scheduler.add_prerequisites(task='A', prerequisites=('B', 'C'))
        # Two possible results:
        #   - A must appears after B and C.
        #   - No requirements on the relative order of B and C.
        schedued_tasks = a_scheduler.schedule()
        self.assertTrue(schedued_tasks in (
            {('B', 'C', 'A')},
            {('C', 'B', 'A')}
        ))

    def test_multiple_linked_lists(self):
        """Test public methods on a task set, which forms two linked lists."""
        a_scheduler = Scheduler()
        # Build the first linked list:
        #   A <- B <- C
        a_scheduler.add_a_prerequisite(task='B', prerequisite='A')
        a_scheduler.add_a_prerequisite(task='C', prerequisite='B')
        # Build the second linked list:
        #   1 <- 2 <- 3
        a_scheduler.add_a_prerequisite(task=2, prerequisite=1)
        a_scheduler.add_a_prerequisite(task=3, prerequisite=2)
        # Only one result is correct.
        scheduled_tasks = a_scheduler.schedule()
        self.assertEqual(scheduled_tasks, {('A', 'B', 'C'), (1, 2, 3)})

    def test_cycle_detection(self):
        """Test public methods on a task set, which forms a cycle."""
        a_scheduler = Scheduler()
        # Build the dependency graph, which is a cycle:
        #   A -> B -> C -> A
        a_scheduler.add_a_prerequisite(task='A', prerequisite='B')
        a_scheduler.add_a_prerequisite(task='B', prerequisite='C')
        a_scheduler.add_a_prerequisite(task='C', prerequisite='A')
        with self.assertRaises(AssertionError):
            a_scheduler.schedule()


if __name__ == "__main__":
    unittest.main()
