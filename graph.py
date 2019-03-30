"""Define classes for building and processing graphs."""


class Union:
    """A container supporting quick union/find operations."""

    def __init__(self):
        """Initialize the underlying data structure."""

    def add(self, i):
        """Add an element labeled by an int to this container."""

    def connect(self, j, k):
        """Connect the two components containing j and k."""

    def connected(self, j, k):
        """Return True if j and k are in the same component.

        Return False, if either of them has not been added.
        """

    def n_elements(self):
        """Return the total number of elements in this container."""


if __name__ == "__main__":
    pass
