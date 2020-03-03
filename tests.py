import unittest
from PythonLinkedlist import *

class Test_tests(unittest.TestCase):
    
    def test_len_SomeNodes_Equal_4(self):
        list=LinkedList()
        n1=Node(12)
        n2=Node(13)
        n3=Node(14)
        n4=Node(-2)
        list.add_in_tail(n1)
        list.add_in_tail(n2)
        list.add_in_tail(n3)
        list.add_in_tail(n4)
        count=list.len()
        self.assertEqual(count,4)

    def test_Len_Empty_List_Is_0(self):
        list=LinkedList()
        count=list.len()
        self.assertEqual(count,0)

    def test_Clean_Make_List_Empty(self):
        list=LinkedList()
        n1=Node(2)
        n2=Node(4)
        n3=Node(5)
        list.add_in_tail(n1)
        list.add_in_tail(n2)
        list.add_in_tail(n3)
        list.clean()
        self.assertEqual(0,list.len())

    def test_Clean_Empty_List_Make_Empty(self):
        list=LinkedList()
        list.clean()
        self.assertEqual(0,list.len())


if __name__ == '__main__':
    unittest.main()

