"""Test Scheduler."""

import unittest

from scheduler import Scheduler


class TestScheduler(unittest.TestCase):
    """Test Scheduler."""

    def test_add_and_count_tasks(self):
        """Test add_a_task(), add_tasks() and count_tasks()."""
        a_scheduler = Scheduler()
        self.assertEqual(a_scheduler.count_tasks(), 0)
        a_scheduler.add_a_task('A')
        self.assertEqual(a_scheduler.count_tasks(), 1)
        a_scheduler.add_a_task('B')
        self.assertEqual(a_scheduler.count_tasks(), 2)
        a_scheduler.add_a_task('B')
        self.assertEqual(a_scheduler.count_tasks(), 2)
        a_scheduler.add_tasks(('C', 'D'))
        self.assertEqual(a_scheduler.count_tasks(), 4)

    def test_add_and_check_dependency(self):
        """Test add_a_prerequisite(), add_prerequisites() and check_dependency()."""
        a_scheduler = Scheduler()
        # No dependency in an empty graph.
        self.assertEqual(a_scheduler.count_tasks(), 0)
        self.assertFalse(a_scheduler.check_dependency('B', 'A'))
        self.assertFalse(a_scheduler.check_dependency('A', 'B'))
        # A unidirectional dependency between two tasks: A <- B.
        a_scheduler.add_a_prerequisite(task='B', prerequisite='A')
        self.assertEqual(a_scheduler.count_tasks(), 2)
        self.assertTrue(a_scheduler.check_dependency('B', 'A'))
        self.assertFalse(a_scheduler.check_dependency('A', 'B'))
        # Make a dependency list: A <- B <- C.
        a_scheduler.add_a_prerequisite(task='C', prerequisite='B')
        self.assertEqual(a_scheduler.count_tasks(), 3)
        self.assertTrue(a_scheduler.check_dependency('C', 'B'))
        self.assertTrue(a_scheduler.check_dependency('B', 'A'))
        # C indirectly depends on A.
        self.assertTrue(a_scheduler.check_dependency('C', 'A'))
        # No dependency in the opposite direction.
        self.assertFalse(a_scheduler.check_dependency('A', 'B'))
        self.assertFalse(a_scheduler.check_dependency('B', 'C'))
        self.assertFalse(a_scheduler.check_dependency('A', 'C'))
        # Add multiple prerequisites.
        a_scheduler.add_prerequisites(task='A', prerequisites=('B', 'C'))
        self.assertEqual(a_scheduler.count_tasks(), 3)
        self.assertTrue(a_scheduler.check_dependency('A', 'B'))
        self.assertTrue(a_scheduler.check_dependency('B', 'C'))
        self.assertTrue(a_scheduler.check_dependency('A', 'C'))

    def test_schedule(self):
        """Test schedule()."""
        a_scheduler = Scheduler()
        a_scheduler.add_a_prerequisite(task='B', prerequisite='A')
        a_scheduler.add_a_prerequisite(task='C', prerequisite='B')
        scheduled_tasks = a_scheduler.schedule()
        self.assertEqual(scheduled_tasks, {('A', 'B', 'C')})
        # Make a dependency graph with multiple independent components.
        a_scheduler.add_a_prerequisite(task=2, prerequisite=1)
        a_scheduler.add_prerequisites(task=3, prerequisites=(2, 1))
        scheduled_tasks = a_scheduler.schedule()
        self.assertEqual(scheduled_tasks, {('A', 'B', 'C'), (1, 2, 3)})
        # Make a cycle in the dependency graph.
        a_scheduler.add_a_prerequisite(task='A', prerequisite='C')
        with self.assertRaises(AssertionError):
            scheduled_tasks = a_scheduler.schedule()


if __name__ == "__main__":
    unittest.main()
