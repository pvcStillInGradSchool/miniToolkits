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
        a_scheduler.add_a_dependency(task='B', prerequisite='A')
        self.assertEqual(a_scheduler.count_tasks(), 2)
        self.assertEqual(a_scheduler.check_dependency('B', 'A'), True)
        self.assertEqual(a_scheduler.check_dependency('A', 'B'), False)
        a_scheduler.add_a_dependency(task='C', prerequisite='A')
        self.assertEqual(a_scheduler.count_tasks(), 3)
        self.assertEqual(a_scheduler.check_dependency('C', 'A'), True)
        self.assertEqual(a_scheduler.check_dependency('A', 'C'), False)

    def test_schedule(self):
        """Test schedule()."""
        a_scheduler = Scheduler()
        a_scheduler.add_a_dependency(task='B', prerequisite='A')
        a_scheduler.add_a_dependency(task='C', prerequisite='B')
        sorted_tasks = a_scheduler.schedule()
        self.assertEqual(len(sorted_tasks), a_scheduler.count_tasks())
        i = 0
        for task_i in sorted_tasks:
            for j in range(i, len(sorted_tasks)):
                task_j = sorted_tasks[j]
                self.assertFalse(a_scheduler.check_dependency(task_i, task_j))
            i += 1


if __name__ == "__main__":
    unittest.main()
