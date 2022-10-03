import unittest
from TaskQueue import TaskQueue, Task


class TestTaskQueue(unittest.TestCase):
    def setUp(self):
        self.t1 = Task(id=1, cycles_left=3)
        self.t2 = Task(id=2, cycles_left=1)
        self.t3 = Task(id=3, cycles_left=5)

        self.tasks = [self.t1, self.t2, self.t3]
        self.TQ = TaskQueue(cycles_per_task=1)
        for task in self.tasks:
            self.TQ.add_task(task)

    def test_remove_task(self):
        with self.assertRaises(RuntimeError):
            self.TQ.remove_task(17)
        self.TQ.remove_task(1)
        self.assertEqual(self.TQ.len, 2)

    def test_execute_tasks(self):
        t_total = self.TQ.execute_tasks()
        self.assertEqual(t_total, 9)


if __name__ == '__main__':
    unittest.main()
