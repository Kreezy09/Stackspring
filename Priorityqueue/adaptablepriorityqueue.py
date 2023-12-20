from heappriorityqueue import HeapPriorityQueue
from empty import Empty

class AdaptableHeapPriorityQueue(HeapPriorityQueue):
    """A locator-based priority queue implemented with a binary heap."""

    # ------------------------------ Nested Locator class ------------------------------

    class Locator(HeapPriorityQueue._Item):
        """Token for locating an entry of the priority queue."""
        __slots__ = '_index'  # add index as an additional field

        def __init__(self, k, v, j):
            super().__init__(k, v)
            self._index = j

        def __iter__(self):
            """Return an iterator for the priority queue."""
            return iter(self._data)
        
        def __reversed__(self):
            """Return a reversed iterator of the priority queue."""
            return reversed(self._data)
    # ------------------------------ Non-public behaviors ------------------------------

    # Override swap to record new indices
    def _swap(self, i, j):
        # Perform the swap
        super()._swap(i, j)
        # Reset locator index (post-swap)
        self._data[i]._index = i
        self._data[j]._index = j

    def _bubble(self, j):
        if j > 0 and self._data[j] < self._data[self._parent(j)]:
            self._upheap(j)
        else:
            self._downheap(j)

    # ------------------------------ Public behaviors ------------------------------

    def add(self, key, value):
        """Add a key-value pair."""
        token = self.Locator(key, value, len(self._data))  # Initialize locator index
        self._data.append(token)
        self._upheap(len(self._data) - 1)
        return token

    def update(self, loc, newkey, newval):
        """Update the key and value for the entry identified by Locator loc."""
        j = loc._index
        if not (0 <= j < len(self) and self._data[j] is loc):
            raise ValueError("Invalid locator")
        loc._key = newkey
        loc._value = newval
        self._bubble(j)

    def remove(self, loc):
        """Remove and return the (key, value) pair identified by Locator loc."""
        j = loc._index
        if not (0 <= j < len(self) and self._data[j] is loc):
            raise ValueError("Invalid locator")
        if j == len(self) - 1:
            # Item at the last position, just remove it
            self._data.pop()
        else:
            # Swap item to the last position
            self._swap(j, len(self) - 1)
            # Remove it from the list
            self._data.pop()
            # Fix item displaced by the swap
            self._bubble(j)
        return loc._key, loc._value
    
    def print_contents(self):
        """Print the contents of the priority queue."""
        print("Priority queue contents:")
        for key, value in [(item._key, item._value) for item in self._data]:
            print(f"({key}, {value})")

    def print_contents_with_locators(self):
        """Print the contents of the priority queue along with locators."""
        print("Priority queue contents with locators:")
        for loc in self._data:
            print(f"Locator: {loc._index}, Key: {loc._key}, Value: {loc._value}")

    def get_locator_for_key(self, key):
        """Get the locator for an element with a given key."""
        for loc in self._data:
            if loc._key == key:
                return loc
        return None

    def get_locator_for_index(self, index):
        """
        Get the locator object for the given index.
        This assumes that your priority queue implementation
        provides a method to retrieve a locator based on an index.
        """
        if 0 <= index < len(self._data):
            return self._data[index]  # Assuming your priority queue stores locators directly
        else:
            raise IndexError("Index out of bounds")


# Test the AdaptableHeapPriorityQueue
# Test the AdaptableHeapPriorityQueue with user input
# adaptable_pq = AdaptableHeapPriorityQueue()

# while True:
#     print("\nOptions:")
#     print("1. Add element")
#     print("2. Update element")
#     print("3. Remove element")
#     print("4. Print contents")
#     print("5. Remove min")
#     print("6. Exit")

#     choice = input("Enter your choice (1-6): ")

#     if choice == '1':
#         key = int(input("Enter key for the new element: "))
#         value = input("Enter value for the new element: ")
#         adaptable_pq.add(key, value)
#     elif choice == '2':
#         try:
#             loc_index = int(input("Enter the index of the element to update: "))
#             loc = adaptable_pq._data[loc_index]
#             new_key = int(input("Enter the new key: "))
#             new_value = input("Enter the new value: ")
#             adaptable_pq.update(loc, new_key, new_value)
#         except (ValueError, IndexError):
#             print("Invalid input. Please enter a valid index.")
#     elif choice == '3':
#         try:
#             loc_index = int(input("Enter the index of the element to remove: "))
#             loc = adaptable_pq._data[loc_index]
#             removed_entry = adaptable_pq.remove(loc)
#             print(f"Removed element: {removed_entry}")
#         except (ValueError, IndexError):
#             print("Invalid input. Please enter a valid index.")
#     elif choice == '4':
#         adaptable_pq.print_contents_with_locators()
#     elif choice == '5':
#         try:
#             removed_entry = adaptable_pq.remove_min()
#             print(f"Removed minimum element: {removed_entry}")
#         except Empty:
#             print("Priority queue is empty.")
#     elif choice == '6':
#         break
#     else:
#         print("Invalid choice. Please enter a number between 1 and 5.")
# def test_get_locator_for_index():
#     # Create an instance of AdaptableHeapPriorityQueue
#     adaptable_pq = AdaptableHeapPriorityQueue()

#     # Add some elements to the priority queue
#     loc1 = adaptable_pq.add(5, 'A')
#     loc2 = adaptable_pq.add(3, 'B')
#     loc3 = adaptable_pq.add(8, 'C')

#     # Print contents with locators
#     print("Initial contents:")
#     adaptable_pq.print_contents_with_locators()

#     try:
#         # Get locator for index 1
#         index_to_get = 1
#         locator_for_index = adaptable_pq.get_locator_for_index(index_to_get)
#         print(f"\nLocator for index {index_to_get}: {locator_for_index._index}, Key: {locator_for_index._key}, Value: {locator_for_index._value}")
#     except IndexError as e:
#         print(f"\nError: {e}")

#     try:
#         # Get locator for index 5 (out of bounds)
#         index_to_get = 5
#         locator_for_index = adaptable_pq.get_locator_for_index(index_to_get)
#         print(f"\nLocator for index {index_to_get}: {locator_for_index._index}, Key: {locator_for_index._key}, Value: {locator_for_index._value}")
#     except IndexError as e:
#         print(f"\nError: {e}")

# if __name__ == "__main__":
#     test_get_locator_for_index()