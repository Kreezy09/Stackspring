from abc import ABC, abstractmethod

class _DoublyLinkedBase:
    """A base class providing a doubly linked list representation."""
    
    class _Node:
        """Lightweight, nonpublic class for storing a doubly linked node."""
        __slots__ = ('_element', '_prev', '_next')  # streamline memory
        
        def __init__(self, element, prev, next):
            """Initialize node's fields."""
            self._element = element  # user's element
            self._prev = prev  # previous node reference
            self._next = next  # next node reference

    def __init__(self):
        """Create an empty list."""
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)  # trailer is after header
        self._header._next = self._trailer  # header is before trailer
        self._trailer._prev = self._header
        self._size = 0  # number of elements

    def __len__(self):
        """Return the number of elements in the list."""
        return self._size

    def is_empty(self):
        """Return True if the list is empty."""
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        """Add element e between two existing nodes and return new node."""
        newest = self._Node(e, predecessor, successor)  # linked to neighbors
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest

    def _delete_node(self, node):
        """Delete nonsentinel node from the list and return its element."""
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1  # record deleted element
        element = node._element
        node._prev = node._next = node._element = None  # deprecate node
        return element
    
class PositionalList(_DoublyLinkedBase):
    """A sequential container of elements allowing positional access."""

    class Position:
        """An abstraction representing the location of a single element."""

        def __init__(self, container, node):
            """Constructor should not be invoked by the user."""
            self._container = container
            self._node = node

        def element(self):
            """Return the element stored at this Position."""
            return self._node._element

        def __eq__(self, other):
            """Return True if other is a Position representing the same location."""
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):
            """Return True if other does not represent the same location."""
            return not (self == other)

    def _validate(self, p):
        """Return position's node, or raise an appropriate error if invalid."""
        if not isinstance(p, self.Position):
            raise TypeError("p must be a proper Position type")
        if p._container is not self:
            raise ValueError("p does not belong to this container")
        if p._node._next is None:
            raise ValueError("p is no longer valid")
        return p._node

    def _make_position(self, node):
        """Return Position instance for the given node (or None if sentinel)."""
        if node is self._header or node is self._trailer:
            return None
        else:
            return self.Position(self, node)

    def first(self):
        """Return the first Position in the list (or None if the list is empty)."""
        return self._make_position(self._header._next)

    def last(self):
        """Return the last Position in the list (or None if the list is empty)."""
        return self._make_position(self._trailer._prev)

    def before(self, p):
        """Return the Position just before Position p (or None if p is the first)."""
        node = self._validate(p)
        return self._make_position(node._prev)

    def after(self, p):
        """Return the Position just after Position p (or None if p is the last)."""
        node = self._validate(p)
        return self._make_position(node._next)

    def __iter__(self):
        """Generate a forward iteration of the elements of the list."""
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

    def _insert_between(self, e, predecessor, successor):
        """Add an element between existing nodes and return a new Position."""
        node = super()._insert_between(e, predecessor, successor)
        return self._make_position(node)

    def add_first(self, e):
        """Insert element e at the front of the list and return a new Position."""
        return self._insert_between(e, self._header, self._header._next)

    def add_last(self, e):
        """Insert element e at the back of the list and return a new Position."""
        return self._insert_between(e, self._trailer._prev, self._trailer)

    def add_before(self, p, e):
        """Insert element e into the list before Position p and return a new Position."""
        original = self._validate(p)
        return self._insert_between(e, original._prev, original)

    def add_after(self, p, e):
        """Insert element e into the list after Position p and return a new Position."""
        original = self._validate(p)
        return self._insert_between(e, original, original._next)

    def delete(self, p):
        """Remove and return the element at Position p."""
        original = self._validate(p)
        return self._delete_node(original)

    def replace(self, p, e):
        """Replace the element at Position p with e. Return the element formerly at Position p."""
        original = self._validate(p)
        old_value = original._element
        original._element = e
        return old_value
    
    def insertion_sort(L):
        """Sort PositionalList of comparable elements into nondecreasing order."""
        if len(L) > 1:
            # otherwise, no need to sort it
            marker = L.first()
            
            while marker != L.last():
                pivot = L.after(marker)  # next item to place
                value = pivot.element()

                if value > marker.element():
                    # pivot is already sorted
                    marker = pivot  # pivot becomes the new marker
                else:
                    # must relocate pivot
                    walk = marker  # find the leftmost item greater than value
                    while walk != L.first() and L.before(walk).element() > value:
                        walk = L.before(walk)

                    L.delete(pivot)  # reinsert value before walk
                    L.add_before(walk, value)


class PriorityQueueBase():
    """Abstract base class for a priority queue."""

    class _Item:
        """Lightweight composite to store priority queue items."""
        
        __slots__ = ('_key', '_value')

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __lt__(self, other):
            """Compare items based on their keys."""
            return self._key < other._key
        
    def is_empty(self):
        """Return True if the priority queue is empty."""
        return len(self) == 0


class SortedPriorityQueue(PriorityQueueBase):
    """A min-oriented priority queue implemented with a sorted list."""
    
    def __init__(self):
        """Create a new empty Priority Queue."""
        self._data = PositionalList()

    def __len__(self):
        """Return the number of items in the priority queue."""
        return len(self._data)

    def add(self, key, value):
        """Add a key-value pair."""
        # make a new item instance
        newest = self._Item(key, value)
        
        # walk backward looking for a smaller key
        walk = self._data.last()
        while walk is not None and newest < walk.element():
            walk = self._data.before(walk)
        
        if walk is None:
            # new key is the smallest
            self._data.add_first(newest)
        else:
            # newest goes after walk
            self._data.add_after(walk, newest)

    def min(self):
        """Return but do not remove (k,v) tuple with the minimum key."""
        if self.is_empty():
            raise Empty("Priority queue is empty.")
        p = self._data.first()
        item = p.element()
        return (item._key, item._value)

    def remove_min(self):
        """Remove and return (k,v) tuple with the minimum key."""
        if self.is_empty():
            raise Empty("Priority queue is empty.")
        item = self._data.delete(self._data.first())
        return (item._key, item._value)
    
class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    pass

# Create a SortedPriorityQueue
sorted_pq = SortedPriorityQueue()

# Add elements with associated keys
sorted_pq.add(3, 'C')
sorted_pq.add(1, 'A')
sorted_pq.add(2, 'B')

# Test min() method
min_element = sorted_pq.min()
print(f"Minimum element: {min_element}")

# Test remove_min() method
removed_element = sorted_pq.remove_min()
print(f"Removed minimum element: {removed_element}")

# Test if the priority queue is empty
print(f"Is the priority queue empty? {sorted_pq.is_empty()}")

# Add more elements
sorted_pq.add(5, 'E')
sorted_pq.add(4, 'D')

# Test iteration through the priority queue
print("Elements in sorted order:")
for key, value in sorted_pq:
    print(f"{key}: {value}")

# Test if the priority queue is empty again
print(f"Is the priority queue empty now? {sorted_pq.is_empty()}")
