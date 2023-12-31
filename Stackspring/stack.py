class ArrayStack:
    def __init__ (self):
        """create empty stack"""
        self._data = [] # nonpublic list instance

    def __len__ (self):        
    #Return the number of elements in the stack.
        return len(self._data)  
        
    def is_empty(self):        
    # Return True if the stack is empty.    
        return len(self._data) == 0
        
    def push(self, e):        
    #Add element e to the top of the stack.        
        self._data.append(e) # new item stored at end of list

        
    def top(self):        
    #Return (but do not remove) the element at the top of the stack.
        if self.is_empty( ):    
            
            raise Empty('Stack is empty')            
        return self._data[-1]# the last item in the list
        
    def pop(self):        
    #Remove and return the element from the top of the stack (i.e., LIFO).        
        if self.is_empty():    
            
            raise Empty('Stack is empty') # remove last item from     list            
        return self._data.pop()
    
    # def print_stack(self):
    #     print("Stack elements:")
    #     for item in reversed(self._data):
    #         print(item)

    
class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    pass