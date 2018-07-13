import unittest
import stack

class TestStackImpl(unittest.TestCase):
    
    def setUp(self):
        self.my_stack = stack.Stack()        
    
    def test_isEmpty(self):
        self.assertEqual(self.my_stack.isEmpty(), True)
        
    def test_push(self):
        self.my_stack.push("Elem")
        self.assertEqual(self.my_stack.isEmpty(), False)
        
    def test_pop(self):
        # test case for empty stack
        elem = self.my_stack.pop()
        self.assertEqual(self.my_stack.isEmpty(), True)
        self.assertEqual(elem, None)
        
        # test case for non-empty stack
        self.my_stack.push("Elem 1")
        self.my_stack.push("Elem 2")
                
        # first pop        
        elem = self.my_stack.pop()
        self.assertEqual(self.my_stack.isEmpty(), False)
        self.assertEqual(elem, "Elem 2")
        
        # second pop
        elem = self.my_stack.pop()
        self.assertEqual(self.my_stack.isEmpty(), True)
        self.assertEqual(elem, "Elem 1")
        
        # third pop
        elem = self.my_stack.pop()
        self.assertEqual(self.my_stack.isEmpty(), True)
        self.assertEqual(elem, None)

if __name__ == '__main__':
    unittest.main()
