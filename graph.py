"""Define classes for building and processing graphs."""


class Union:
    """A container supporting quick union/find operations."""

    def __init__(self):
        """Initialize the underlying data structure."""
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
        return self._root(j) == self._root(k)

    def n_elements(self):
        """Return the total number of elements in this container."""
        return len(self._size)

    def _has(self, i):
        return i < self.n_elements()

    def _root(self, i):
        while i != self._parent[i]:
            # Compress the path to make the tree flatter.
            grand_parent = self._parent[self._parent[i]]
            self._parent[i] = grand_parent
            # Update i and try the next iteration.
            i = grand_parent
        return i

    def _compare_tree(self, j, k):
        root_j = self._root(j)
        root_k = self._root(k)
        if self._size[root_j] < self._size[root_k]:
            return root_j, root_k
        return root_k, root_j


if __name__ == "__main__":
    pass
