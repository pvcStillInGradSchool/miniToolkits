"""Test classes defined in graph.py."""

import unittest

from graph import DirectedGraph
from graph import Reachability
from graph import UnionFind


class TestDirectedGraph(unittest.TestCase):
    """Test the correctness of graph.DirectedGraph."""

    def test_initialization(self):
        """Test public methods on an empty union."""
        # Create [].
        an_empty_graph = DirectedGraph()
        self.assertEqual(an_empty_graph.n_vertices(), 0)
        self.assertEqual(an_empty_graph.connected(0, 0), False)
        self.assertEqual(an_empty_graph.connected(0, 1), False)
        self.assertEqual(an_empty_graph.neighbors(0), set())

    def test_consecutive_adding(self):
        """Test adding vertices consecutively."""
        # Create [].
        a_graph = DirectedGraph()
        # Add 0 to [], which becomes [set()].
        a_graph.add(0)
        self.assertEqual(a_graph.n_vertices(), 1)
        self.assertEqual(a_graph.connected(0, 0), True)
        self.assertEqual(a_graph.connected(0, 1), False)
        self.assertEqual(a_graph.connected(1, 1), False)
        # Add 0 to [set()], nothing changes.
        a_graph.add(0)
        self.assertEqual(a_graph.n_vertices(), 1)
        self.assertEqual(a_graph.connected(0, 0), True)
        self.assertEqual(a_graph.connected(0, 1), False)
        self.assertEqual(a_graph.connected(1, 1), False)
        # Add 1 to [set()], which becomes [set(), set()].
        a_graph.add(1)
        self.assertEqual(a_graph.n_vertices(), 2)
        self.assertEqual(a_graph.connected(0, 0), True)
        self.assertEqual(a_graph.connected(0, 1), False)
        self.assertEqual(a_graph.connected(1, 1), True)

    def test_non_consecutive_adding(self):
        """Test adding vertices non-consecutively."""
        # Create [].
        a_graph = DirectedGraph()
        # Add 1 to [], which becomes [set(), set()].
        # Here 0 is added implicitly.
        a_graph.add(1)
        self.assertEqual(a_graph.n_vertices(), 2)
        self.assertEqual(a_graph.connected(0, 0), True)
        self.assertEqual(a_graph.connected(0, 1), False)
        self.assertEqual(a_graph.connected(1, 1), True)

    def test_implicit_adding_by_connecting(self):
        """Test connect(), which implicitly calls add()."""
        # Create [].
        a_graph = DirectedGraph()
        # Implicitly add 0, 1, 2 to [], then connect 1 with 2,
        # which makes [set(), {2}, set()].
        a_graph.connect(1, 2)
        self.assertEqual(a_graph.n_vertices(), 3)
        # Trivially connected vertices.
        self.assertEqual(a_graph.connected(0, 0), True)
        self.assertEqual(a_graph.connected(1, 1), True)
        self.assertEqual(a_graph.connected(2, 2), True)
        # Uni-directional connection created by connect().
        self.assertEqual(a_graph.connected(1, 2), True)
        self.assertEqual(a_graph.connected(2, 1), False)
        # Disconnected vertices.
        self.assertEqual(a_graph.connected(0, 1), False)
        self.assertEqual(a_graph.connected(1, 0), False)
        self.assertEqual(a_graph.connected(0, 2), False)
        self.assertEqual(a_graph.connected(2, 0), False)

    def test_neighbors(self):
        """Test root()."""
        # Create [{1, 2}, {2}, set()].
        a_graph = DirectedGraph()
        a_graph.connect(0, 1)
        a_graph.connect(0, 2)
        a_graph.connect(1, 2)
        # Check neighbors on existing vertices.
        self.assertEqual(a_graph.neighbors(0), {1, 2})
        self.assertEqual(a_graph.neighbors(1), {2})
        self.assertEqual(a_graph.neighbors(2), set())
        # Check neighbors on non-existing vertices.
        self.assertEqual(a_graph.neighbors(3), set())
        self.assertEqual(a_graph.neighbors(4), set())


class TestReachability(unittest.TestCase):
    """Test the correctness of graph.Reachability."""

    def test_empty_graph(self):
        """Test public methods on an empty graph."""
        # Build an empty graph.
        a_graph = DirectedGraph()
        checker = Reachability(a_graph)
        # Non-existing vertex is always NOT reachable.
        self.assertFalse(checker.has_path(0, 0))
        self.assertFalse(checker.has_path(0, 1))

    def test_linked_list(self):
        """Test public methods on a linked list."""
        # Build a linked list:
        #   0 -> 1 -> 2
        a_graph = DirectedGraph()
        a_graph.connect(0, 1)
        a_graph.connect(1, 2)
        checker = Reachability(a_graph)
        # A vertex is always reachable from/to itself.
        self.assertTrue(checker.has_path(0, 0))
        self.assertTrue(checker.has_path(1, 1))
        self.assertTrue(checker.has_path(2, 2))
        # A downstream vertex is reachable from an upstream vertex.
        self.assertTrue(checker.has_path(0, 1))
        self.assertTrue(checker.has_path(1, 2))
        self.assertTrue(checker.has_path(0, 2))
        # A upstream vertex is NOT reachable from an downstream vertex.
        self.assertFalse(checker.has_path(1, 0))
        self.assertFalse(checker.has_path(2, 0))
        self.assertFalse(checker.has_path(2, 1))

    def test_binary_tree(self):
        """Test public methods on a binary tree."""
        # Build a binary tree:
        #     0
        #    / \
        #   1   2
        a_graph = DirectedGraph()
        a_graph.connect(0, 1)
        a_graph.connect(0, 2)
        checker = Reachability(a_graph)
        # All the vertices are reachable from the root.
        self.assertTrue(checker.has_path(0, 1))
        self.assertTrue(checker.has_path(0, 2))
        # Vertices in another subtree are NOT reachable.
        self.assertFalse(checker.has_path(1, 2))
        self.assertFalse(checker.has_path(2, 1))
        # Parent is NOT reachable.
        self.assertFalse(checker.has_path(1, 0))
        self.assertFalse(checker.has_path(2, 0))

class TestUnionFind(unittest.TestCase):
    """Test the correctness of graph.UnionFind."""

    def test_initialization(self):
        """Test public methods on an empty union."""
        # Create { }.
        an_empty_graph = UnionFind()
        self.assertEqual(an_empty_graph.n_vertices(), 0)
        self.assertEqual(an_empty_graph.connected(0, 0), False)
        self.assertEqual(an_empty_graph.connected(0, 1), False)

    def test_consecutive_adding(self):
        """Test adding vertices consecutively."""
        # Create { }.
        a_graph = UnionFind()
        # Add 0 to { }, which becomes { {0} }.
        a_graph.add(0)
        self.assertEqual(a_graph.n_vertices(), 1)
        self.assertEqual(a_graph.connected(0, 0), True)
        self.assertEqual(a_graph.connected(0, 1), False)
        self.assertEqual(a_graph.connected(1, 1), False)
        # Add 0 to { {0} }, nothing changes.
        a_graph.add(0)
        self.assertEqual(a_graph.n_vertices(), 1)
        self.assertEqual(a_graph.connected(0, 0), True)
        self.assertEqual(a_graph.connected(0, 1), False)
        self.assertEqual(a_graph.connected(1, 1), False)
        # Add 1 to { {0} }, which becomes { {0}, {1} }.
        a_graph.add(1)
        self.assertEqual(a_graph.n_vertices(), 2)
        self.assertEqual(a_graph.connected(0, 0), True)
        self.assertEqual(a_graph.connected(0, 1), False)
        self.assertEqual(a_graph.connected(1, 1), True)

    def test_non_consecutive_adding(self):
        """Test adding vertices non-consecutively."""
        # Create { }.
        a_graph = UnionFind()
        # Add 1 to { }, which becomes { {0}, {1} }.
        # Here 0 is added implicitly.
        a_graph.add(1)
        self.assertEqual(a_graph.n_vertices(), 2)
        self.assertEqual(a_graph.connected(0, 0), True)
        self.assertEqual(a_graph.connected(0, 1), False)
        self.assertEqual(a_graph.connected(1, 1), True)

    def test_implicit_adding_by_connecting(self):
        """Test connect(), which implicitly calls add()."""
        # Create { }.
        a_graph = UnionFind()
        # Implicitly add 0, 1, 2 to { }, then connect 1 with 2,
        # which makes { {0}, {1, 2} }.
        a_graph.connect(1, 2)
        self.assertEqual(a_graph.n_vertices(), 3)
        # Trivially connected components.
        self.assertEqual(a_graph.connected(0, 0), True)
        self.assertEqual(a_graph.connected(1, 1), True)
        self.assertEqual(a_graph.connected(2, 2), True)
        # Connected components created by connect().
        self.assertEqual(a_graph.connected(1, 2), True)
        self.assertEqual(a_graph.connected(2, 1), True)
        # Disconnected components.
        self.assertEqual(a_graph.connected(0, 1), False)
        self.assertEqual(a_graph.connected(1, 0), False)
        self.assertEqual(a_graph.connected(0, 2), False)
        self.assertEqual(a_graph.connected(2, 0), False)

    def test_root(self):
        """Test root()."""
        # Create { {0}, {1, 2} }.
        a_graph = UnionFind()
        a_graph.connect(1, 2)
        # Check legal input.
        self.assertEqual(a_graph.root(0), 0)
        self.assertTrue(a_graph.root(1) in {1, 2})
        self.assertTrue(a_graph.root(2) in {1, 2})
        # Check illegal input.
        with self.assertRaises(AssertionError):
            a_graph.root(3)


if __name__ == "__main__":
    unittest.main()
