"""Test classes defined in graph.py."""

import unittest

import graph


class TestUnion(unittest.TestCase):
    """Test the correctness of graph.Union."""

    def test_initialization(self):
        """Test public methods on an empty union."""
        # Create { }.
        an_empty_union = graph.Union()
        self.assertEqual(an_empty_union.n_elements(), 0)
        self.assertEqual(an_empty_union.connected(0, 0), False)
        self.assertEqual(an_empty_union.connected(0, 1), False)

    def test_consecutive_adding(self):
        """Test adding elements consecutively."""
        # Create { }.
        a_union = graph.Union()
        # Add 0 to { }, which becomes { {0} }.
        a_union.add(0)
        self.assertEqual(a_union.n_elements(), 1)
        self.assertEqual(a_union.connected(0, 0), True)
        self.assertEqual(a_union.connected(0, 1), False)
        self.assertEqual(a_union.connected(1, 1), False)
        # Add 0 to { {0} }, nothing changes.
        a_union.add(0)
        self.assertEqual(a_union.n_elements(), 1)
        self.assertEqual(a_union.connected(0, 0), True)
        self.assertEqual(a_union.connected(0, 1), False)
        self.assertEqual(a_union.connected(1, 1), False)
        # Add 1 to { {0} }, which becomes { {0}, {1} }.
        a_union.add(1)
        self.assertEqual(a_union.n_elements(), 2)
        self.assertEqual(a_union.connected(0, 0), True)
        self.assertEqual(a_union.connected(0, 1), False)
        self.assertEqual(a_union.connected(1, 1), True)

    def test_non_consecutive_adding(self):
        """Test adding elements non-consecutively."""
        # Create { }.
        a_union = graph.Union()
        # Add 1 to { }, which becomes { {0}, {1} }.
        # Here 0 is added implicitly.
        a_union.add(1)
        self.assertEqual(a_union.n_elements(), 2)
        self.assertEqual(a_union.connected(0, 0), True)
        self.assertEqual(a_union.connected(0, 1), False)
        self.assertEqual(a_union.connected(1, 1), True)

    def test_implicit_adding_by_connecting(self):
        """Test connect(), which implicitly calls add()."""
        # Create { }.
        a_union = graph.Union()
        # Implicitly add 0, 1, 2 to { }, then connect 1 with 2,
        # which makes { {0}, {1, 2} }.
        a_union.connect(1, 2)
        self.assertEqual(a_union.n_elements(), 3)
        # Trivially connected components.
        self.assertEqual(a_union.connected(0, 0), True)
        self.assertEqual(a_union.connected(1, 1), True)
        self.assertEqual(a_union.connected(2, 2), True)
        # Connected components created by connect().
        self.assertEqual(a_union.connected(1, 2), True)
        self.assertEqual(a_union.connected(2, 1), True)
        # Disconnected components.
        self.assertEqual(a_union.connected(0, 1), False)
        self.assertEqual(a_union.connected(1, 0), False)
        self.assertEqual(a_union.connected(0, 2), False)
        self.assertEqual(a_union.connected(2, 0), False)

    def test_root(self):
        """Test root()."""
        # Create { {0}, {1, 2} }.
        a_union = graph.Union()
        a_union.connect(1, 2)
        # Check legal input.
        self.assertEqual(a_union.root(0), 0)
        self.assertTrue(a_union.root(1) in {1, 2})
        self.assertTrue(a_union.root(2) in {1, 2})
        # Check illegal input.
        with self.assertRaises(AssertionError):
            a_union.root(3)


if __name__ == "__main__":
    unittest.main()
