"""Test Scheduler."""

import unittest

from scheduler import Scheduler


class TestScheduler(unittest.TestCase):
    """Test Scheduler."""

    def test_add_and_count_tasks(self):
        """Test add_a_task() and count_tasks()."""
        a_scheduler = Scheduler()
        self.assertEqual(a_scheduler.count_tasks(), 0)
        a_scheduler.add_a_task('A')
        self.assertEqual(a_scheduler.count_tasks(), 1)
        a_scheduler.add_a_task('B')
        self.assertEqual(a_scheduler.count_tasks(), 2)
        a_scheduler.add_a_task('B')
        self.assertEqual(a_scheduler.count_tasks(), 2)

    def test_add_and_count_dependency(self):
        """Test add_a_dependency() and count_dependencies()."""
        a_scheduler = Scheduler()
        self.assertEqual(a_scheduler.count_tasks(), 0)
        self.assertEqual(a_scheduler.check_dependency('B', 'A'), False)
        self.assertEqual(a_scheduler.check_dependency('A', 'B'), False)
        a_scheduler.add_a_dependency(task='B', dependency='A')
        self.assertEqual(a_scheduler.count_tasks(), 2)
        self.assertEqual(a_scheduler.check_dependency('B', 'A'), True)
        self.assertEqual(a_scheduler.check_dependency('A', 'B'), False)
        a_scheduler.add_a_dependency(task='C', dependency='A')
        self.assertEqual(a_scheduler.count_tasks(), 3)
        self.assertEqual(a_scheduler.check_dependency('C', 'A'), True)
        self.assertEqual(a_scheduler.check_dependency('A', 'C'), False)

    def test_schedule(self):
        """Test schedule()."""
        self.fail()


if __name__ == "__main__":
    unittest.main()
