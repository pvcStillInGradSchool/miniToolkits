"""Define classes for building and processing graphs."""


class DirectedGraph:
    
    def __init__(self):
        # Suppose vertex[i] is the i-th vertex, then
        # _neighbor[i] is the set of neighbors of vertex[i]
        self._neighbor = list()
    
    def n_elements(self):
        """Return the total number of elements in this graph."""
        return len(self._neighbor)

    def add(self, i):
        """Add an element labeled by an int to this container."""
        assert isinstance(i, int) and i >= 0
        while not self._has(i):
            self._neighbor.append(set())

    def connect(self, j, k):
        """Connect element[j] to element[k]."""
        self.add(j)
        self.add(k)
        self._neighbor[j].add(k)

    def connected(self, j, k):
        """Return True if element[k] is a neighbor of element[j].

        Return False, if either of them has not been added.
        """
        if (not self._has(j)) or (not self._has(k)):
            return False
        if j == k:
            return True
        return k in self._neighbor[j]

    def neighbors(self, i):
        """Return a set containing element[i]'s neighbors."""
        if self._has(i):
            return frozenset(self._neighbor[i])
        return frozenset()

    def _has(self, i):
        return i < self.n_elements()


class UnionFind:
    """A container supporting quick union/find operations."""

    def __init__(self):
        # Suppose element[i] is the i-th element.
        # _parent[i] is the id of the parent of element[i].
        self._parent = list()
        # _size[i] is the size of the largest tree containing element[i].
        self._size = list()

    def add(self, i):
        """Add an element labeled by an int to this container."""
        assert isinstance(i, int) and i >= 0
        while not self._has(i):
            self._parent.append(self.n_elements())
            self._size.append(1)

    def connect(self, j, k):
        """Connect the two components containing j and k."""
        self.add(j)
        self.add(k)
        root_smaller, root_larger = self._compare_tree(j, k)
        self._parent[root_smaller] = root_larger
        self._size[root_larger] += self._size[root_smaller]

    def connected(self, j, k):
        """Return True if j and k are in the same component.

        Return False, if either of them has not been added.
        """
        if (not self._has(j)) or (not self._has(k)):
            return False
        return self.root(j) == self.root(k)

    def n_elements(self):
        """Return the total number of elements in this container."""
        return len(self._size)

    def _has(self, i):
        return i < self.n_elements()

    def root(self, i):
        """Return the root of the tree containing i."""
        assert self._has(i), "{0} is not in this container.".format(i)
        while i != self._parent[i]:
            # Compress the path to make the tree flatter.
            grand_parent = self._parent[self._parent[i]]
            self._parent[i] = grand_parent
            # Update i and try the next iteration.
            i = grand_parent
        return i

    def _compare_tree(self, j, k):
        root_j = self.root(j)
        root_k = self.root(k)
        if self._size[root_j] < self._size[root_k]:
            return root_j, root_k
        return root_k, root_j


if __name__ == "__main__":
    pass
