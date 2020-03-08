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

    def test_insert_after(self):
        list=LinkedList()
        n1=Node(3)
        n2=Node(4)
        n3=Node(6)
        n4=Node(-1)
        list.add_in_tail(n1)
        list.add_in_tail(n2)
        list.add_in_tail(n3)
        list.insert(n2,n4)
        self.assertEqual(4,list.len())

    def test_insert_after_tail(self):
        list=LinkedList()
        n1=Node(3)
        n2=Node(4)
        n3=Node(5)
        n4=Node(0)
        list.add_in_tail(n1)
        list.add_in_tail(n2)
        list.add_in_tail(n3)
        list.insert(n3,n4)
        self.assertEqual(4,list.len())

    def test_insert_after_not_exist_node(self):
        list=LinkedList()
        n1=Node(5)
        n2=Node(5)
        n0=Node(3)
        n3=Node(5)
        n4=Node(-1)
        list.add_in_tail(n1)
        list.add_in_tail(n2)
        list.add_in_tail(n3)
        list.insert(n0,n4)
        self.assertEqual(3,list.len())

    def test_find_all(self):
        list=LinkedList()
        n1=Node(2)
        n2=Node(1)
        n3=Node(3)
        n4=Node(5)
        n5=Node(5)
        list.add_in_tail(n1)
        list.add_in_tail(n2)
        list.add_in_tail(n3)
        list.add_in_tail(n4)
        list.add_in_tail(n5)
        elements=list.find_all(n4.value)
        self.assertEqual([n4,n5],elements)

    def test_find_all_not_exists(self):
        list=LinkedList()
        n1=Node(2)
        n2=Node(1)
        n3=Node(3)
        n4=Node(5)
        n5=Node(5)
        list.add_in_tail(n1)
        list.add_in_tail(n2)
        list.add_in_tail(n3)
        list.add_in_tail(n4)
        list.add_in_tail(n5)
        elements=list.find_all(-2)
        self.assertEqual([],elements)
    
    def test_find_all_if_all_same_as_list(self):
        list=LinkedList()
        n1=Node(1)
        n2=Node(1)
        n3=Node(1)
        n4=Node(1)
        n5=Node(1)
        list.add_in_tail(n1)
        list.add_in_tail(n2)
        list.add_in_tail(n3)
        list.add_in_tail(n4)
        list.add_in_tail(n5)
        elements=list.find_all(1)
        self.assertEqual([n1,n2,n3,n4,n5],elements)

    def test_delete_node_single_from_head(self):
        list=LinkedList()
        n1=Node(1)
        n2=Node(2)
        n3=Node(3)
        n4=Node(4)
        n5=Node(5)
        list.add_in_tail(n1)
        list.add_in_tail(n2)
        list.add_in_tail(n3)
        list.add_in_tail(n4)
        list.add_in_tail(n5)
        list.delete(1)
        self.assertEqual(4,list.len())

    def test_delete_node_single_from_middle(self):
        list=LinkedList()
        n1=Node(1)
        n2=Node(2)
        n3=Node(3)
        n4=Node(4)
        n5=Node(5)
        list.add_in_tail(n1)
        list.add_in_tail(n2)
        list.add_in_tail(n3)
        list.add_in_tail(n4)
        list.add_in_tail(n5)
        list.delete(4)
        self.assertEqual(4,list.len())

    def test_delete_node_single_from_tail_false(self):
        list=LinkedList()
        n1=Node(1)
        n2=Node(2)
        n3=Node(3)
        n4=Node(4)
        n5=Node(5)
        list.add_in_tail(n1)
        list.add_in_tail(n2)
        list.add_in_tail(n3)
        list.add_in_tail(n4)
        list.add_in_tail(n5)
        list.delete(5)
        self.assertEqual(4,list.len())

    def test_delete_not_existed_single(self):
        list=LinkedList()
        n1=Node(1)
        n2=Node(2)
        n3=Node(3)
        n4=Node(4)
        n5=Node(5)
        list.add_in_tail(n1)
        list.add_in_tail(n2)
        list.add_in_tail(n3)
        list.add_in_tail(n4)
        list.add_in_tail(n5)
        list.delete(7)
        self.assertEqual(5,list.len())

    def test_delete_not_existed_All(self):
        list=LinkedList()
        n1=Node(1)
        n2=Node(2)
        n3=Node(3)
        n4=Node(4)
        n5=Node(5)
        list.add_in_tail(n1)
        list.add_in_tail(n2)
        list.add_in_tail(n3)
        list.add_in_tail(n4)
        list.add_in_tail(n5)
        list.delete(7,True)
        self.assertEqual(5,list.len())
    
    def test_delete_all_existed_nodes(self):
        list=LinkedList()
        n1=Node(1)
        n2=Node(2)
        n3=Node(1)
        n4=Node(4)
        n5=Node(1)
        list.add_in_tail(n1)
        list.add_in_tail(n2)
        list.add_in_tail(n3)
        list.add_in_tail(n4)
        list.add_in_tail(n5)
        list.delete(1,True)
        self.assertEqual(2,list.len())

    def test_delete_single_element(self):
        list=LinkedList()
        n1=Node(1)
        list.add_in_tail(n1)
        list.delete(1)
        self.assertEqual(0,list.len())

    def test_delete_single_element_true(self):
        list=LinkedList()
        n1=Node(1)
        list.add_in_tail(n1)
        list.delete(1,True)
        self.assertEqual(0,list.len())

    def test_delete_single_at_tail_true(self):
        list=LinkedList()
        n1=Node(1)
        n2=Node(2)
        n3=Node(3)
        n4=Node(4)
        n5=Node(5)
        list.add_in_tail(n1)
        list.add_in_tail(n2)
        list.add_in_tail(n3)
        list.add_in_tail(n4)
        list.add_in_tail(n5)
        list.delete(5,True)
        self.assertEqual(4,list.len())

    def test_delete_single_at_middle_true(self):
        list=LinkedList()
        n1=Node(1)
        n2=Node(2)
        n3=Node(3)
        n4=Node(4)
        n5=Node(5)
        list.add_in_tail(n1)
        list.add_in_tail(n2)
        list.add_in_tail(n3)
        list.add_in_tail(n4)
        list.add_in_tail(n5)
        list.delete(3,True)
        self.assertEqual(4,list.len())

    def test_delete_empty_list_true(self):
        list=LinkedList()
        list.delete(3,True)
        self.assertEqual(0,list.len())

    def test_delete_empty_list_false(self):
        list=LinkedList()
        list.delete(3)
        self.assertEqual(0,list.len())

    def test_delete_all_nodes_by_delete_true(self):
        list=LinkedList()
        n1=Node(1)
        n2=Node(1)
        n3=Node(1)
        n4=Node(1)
        n5=Node(1)
        list.add_in_tail(n1)
        list.add_in_tail(n2)
        list.add_in_tail(n3)
        list.add_in_tail(n4)
        list.add_in_tail(n5)
        list.delete(1,True)
        self.assertEqual(0,list.len())

    def test_delete_almost_nodes_by_delete_true(self):
        list=LinkedList()
        n1=Node(1)
        n2=Node(1)
        n3=Node(1)
        n4=Node(1)
        n5=Node(2)
        list.add_in_tail(n1)
        list.add_in_tail(n2)
        list.add_in_tail(n3)
        list.add_in_tail(n4)
        list.add_in_tail(n5)
        list.delete(1,True)
        self.assertEqual(1,list.len())

    def test_delete_almost_in_middle(self):
        list=LinkedList()
        n1=Node(2)
        n2=Node(2)
        n3=Node(1)
        n4=Node(2)
        n5=Node(2)
        list.add_in_tail(n1)
        list.add_in_tail(n2)
        list.add_in_tail(n3)
        list.add_in_tail(n4)
        list.add_in_tail(n5)
        list.delete(2,True)
        self.assertEqual(1,list.len())

    def test_delete_almost_nodes_from_tail_true(self):
        list=LinkedList()
        n1=Node(1)
        n2=Node(2)
        n3=Node(2)
        n4=Node(2)
        n5=Node(2)
        list.add_in_tail(n1)
        list.add_in_tail(n2)
        list.add_in_tail(n3)
        list.add_in_tail(n4)
        list.add_in_tail(n5)
        list.delete(2,True)
        list.print_all_nodes()
        self.assertEqual(1,list.len())

    def test_insert_into_empty_list(self):
         list=LinkedList()
         n1=Node(10)
         list.insert(None,n1)
         self.assertEqual(1,list.len())

    def test_insert_None(self):
        list=LinkedList()
        n1=Node(10)
        list.add_in_tail(n1)
        list.insert(n1,None)
        self.assertEqual(1,list.len())

    def test_insert_in_tail(self):
        list=LinkedList()
        n1=Node(10)
        n2=Node(11)
        n3=Node(12)
        n4=Node(-1)
        list.add_in_tail(n1)
        list.add_in_tail(n2)
        list.add_in_tail(n3)
        list.insert(n3,n4)
        self.assertEqual(4,list.len())

    def test_insert_in_middle(self):
        list=LinkedList()
        n1=Node(10)
        n2=Node(11)
        n3=Node(12)
        n4=Node(-1)
        list.add_in_tail(n1)
        list.add_in_tail(n2)
        list.add_in_tail(n3)
        list.insert(n1,n4)
        self.assertEqual(4,list.len())

    def test_insert_after_None(self):
        list=LinkedList()
        n1=Node(10)
        n2=Node(11)
        n3=Node(12)
        n4=Node(-1)
        list.add_in_tail(n1)
        list.add_in_tail(n2)
        list.add_in_tail(n3)
        list.insert(None,n4)
        self.assertEqual(3,list.len())
        list.print_all_nodes()

     


if __name__ == '__main__':
    unittest.main()

