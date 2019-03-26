"""Test Scheduler."""

import unittest

from scheduler import Scheduler


class TestScheduler(unittest.TestCase):
    """Test Scheduler."""

    def test_add_and_count_tasks(self):
        """Test add_tasks() and count_tasks()."""
        a_scheduler = Scheduler()
        self.assertEqual(a_scheduler.count_tasks(), 0)
        a_scheduler.add_task('A')
        self.assertEqual(a_scheduler.count_tasks(), 1)
        a_scheduler.add_task('B')
        self.assertEqual(a_scheduler.count_tasks(), 2)
        a_scheduler.add_task('B')
        self.assertEqual(a_scheduler.count_tasks(), 2)

    def test_add_and_count_dependency(self):
        """Test add_dependency() and count_dependencies()."""
        self.fail()

    def test_schedule(self):
        """Test schedule()."""
        self.fail()


if __name__ == "__main__":
    unittest.main()
