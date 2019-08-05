#
# A simple stack implementation
#

class Stack():
        
    def __init__(self):
        self._elements = []
        
    def isEmpty(self):
        return len(self._elements) == 0
    
    def push(self, elem):
        self._elements.append(elem)
        
    def pop(self):
        if not self.isEmpty():
            return self._elements.pop()
        else:
            return None
        

if __name__ == '__main__':
    my_stack = Stack()
    my_stack.push("!")
    my_stack.push("World")
    my_stack.push("Hello")
    
    while not my_stack.isEmpty():
        print(my_stack.pop(), end=" ")
    print()
    
    
