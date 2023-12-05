import positionalList as psl

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
        self._data = psl.PositionalList()

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
    
    def remove(self, priority, name):
        """Remove a patient with the specified priority and name."""
        walk = self._data.first()
        while walk is not None:
            item = walk.element()
            if item._key == priority and item._value == name:
                self._data.delete(walk)
                return
            walk = self._data.after(walk)

        raise ValueError(f"Patient with priority {priority} and name {name} not found.")

    
    def __iter__(self):
        """Generate a forward iteration of the elements in sorted order."""
        for item in self._data:
            yield (item._key, item._value)

    def __reversed__(self):
        """Return a reversed iterator of the elements."""
        return reversed([(item._key, item._value) for item in self._data])
            
    def update_priority(self, old_priority, old_name, new_priority):
        """Update the priority (key) of a previously entered patient (value)."""
        walk = self._data.first()
        while walk is not None:
            item = walk.element()
            if item._key == old_priority and item._value == old_name:
                # Remove the old item
                self._data.delete(walk)
                # Add a new item with the updated priority
                self.add(new_priority, old_name)
                return
            walk = self._data.after(walk)

        raise ValueError(f"Patient with priority {old_priority} and name {old_name} not found.")

    def print_contents(self):
        """Print the contents of the queue."""
        for item in self._data:
            print(f"Priority: {item._key}, Name: {item._value}")

        
class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    pass

# priority_queue = SortedPriorityQueue()

# # Add some patients
# priority_queue.add(3, "Alice")
# priority_queue.add(1, "Bob")
# priority_queue.add(2, "Charlie")

# # Print the initial contents
# print("Initial Contents:")
# priority_queue.print_contents()

# # Update the priority of a patient
# priority_queue.update_priority(1, "Bob", 4)

# # Print the updated contents
# print("\nUpdated Contents:")
# priority_queue.print_contents()
# Create a SortedPriorityQueue
# test_priority_queue.py

# sorted_pq = SortedPriorityQueue()

# # Get input for key-value pairs
# num_elements = int(input("Enter the number of elements: "))

# for _ in range(num_elements):
#     key = int(input("Enter the priority (an integer): "))
#     value = input("Enter the value: ")
#     sorted_pq.add(key, value)

# # Test min() method
# try:
#     min_element = sorted_pq.min()
#     print(f"Minimum element: {min_element}")
# except Empty as e:
#     print(f"Error: {e}")

# # Test remove_min() method
# try:
#     removed_element = sorted_pq.remove_min()
#     print(f"Removed minimum element: {removed_element}")
# except Empty as e:
#     print(f"Error: {e}")

# # Test if the priority queue is empty
# print(f"Is the priority queue empty? {sorted_pq.is_empty()}")

# # Add more elements
# num_additional_elements = int(input("Enter the number of additional elements: "))

# for _ in range(num_additional_elements):
#     key = int(input("Enter the priority (an integer): "))
#     value = input("Enter the value: ")
#     sorted_pq.add(key, value)

# # Test iteration through the priority queue
# print("Elements in sorted order:")
# for key, value in sorted_pq:
#     print(f"{key}: {value}")

# # Test if the priority queue is empty again
# print(f"Is the priority queue empty now? {sorted_pq.is_empty()}")
