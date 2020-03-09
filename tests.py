import unittest
from LinkedListTwoWay import *


class Test_tests(unittest.TestCase):

    def When_ListIsEmpty_Len_Should_BeZero(self):
        list=LinkedList2()
        self.assertEqual(list.len(),0)

    def When_ListIsNotEmptyAndHasFiveElements_Len_Should_ProvideFiveValue(self):
        list=LinkedList2()
        n1=Node(1)
        n2=Node(2)
        n3=Node(3)
        n4=Node(4)
        n5=Node(5)
        n1.next=n2
        n2.prev=n1
        n2.next=n3
        n3.prev=n2
        n3.next=n4
        n4.prev=n3
        n4.next=n5
        n5.prev=n4
        list.add_in_tail(n1)
        list.add_in_tail(n2)
        list.add_in_tail(n3)
        list.add_in_tail(n4)
        list.add_in_tail(n5)
        self.assertEqual(list.len(),5)

    def When_ListIsEmpty_AddInHead_MustBeAdded(self):
        list=LinkedList2()
        n1=Node(1)
        list.add_in_head(n1)
        self.assertEqual(list.len(),1)
        self.asserEqual(list.head.value,1)

    def When_ListIsNotEmpty_AddInHead_MustChangeCurrentHead(self):
        list=LinkedList2()
        n1=Node(1)
        n2=Node(2)
        n3=Node(3)
        n4=Node(4)
        n1.next=n2
        n2.prev=n1
        n2.next=n3
        n3.prev=n2
        n3.next=n4
        n4.prev=n3
        list.add_in_tail(n1)
        list.add_in_tail(n2)
        list.add_in_tail(n3)
        list.add_in_tail(n4)
        newHead=Node(100)
        list.add_in_head(newHead)
        self.assertEqual(list.len(),5)
        self.asserEqual(list.head.value,100)

    def When_ListIsEmpty_Clean_MustMakeListAllEmpty(self):
        list=LinkedList2()
        list.clean()
        self.assertEqual(list.len(),0)
        self.assertEqual(list.head,None)
        self.assertEqual(list.tail,None)

    def When_ListIsNotEmpty_Clean_MustMakeListEmpty(self):
        list=LinkedList2()
        n1=Node(1)
        n2=Node(2)
        n3=Node(3)
        n4=Node(4)
        n5=Node(5)
        n1.next=n2
        n2.prev=n1
        n2.next=n3
        n3.prev=n2
        n3.next=n4
        n4.prev=n3
        n4.next=n5
        n5.prev=n4
        list.add_in_tail(n1)
        list.add_in_tail(n2)
        list.add_in_tail(n3)
        list.add_in_tail(n4)
        list.add_in_tail(n5)
        list.clean()
        self.assertEqual(list.len(),0)
        self.assertEqual(list.head,None)
        self.assertEqual(list.tail,None)

    def When_ListContainsValue_Find_MustReturnItem(self):
        list=LinkedList2()
        n1=Node(1)
        n2=Node(2)
        n3=Node(3)
        n4=Node(4)
        n5=Node(5)
        n1.next=n2
        n2.prev=n1
        n2.next=n3
        n3.prev=n2
        n3.next=n4
        n4.prev=n3
        n4.next=n5
        n5.prev=n4
        list.add_in_tail(n1)
        list.add_in_tail(n2)
        list.add_in_tail(n3)
        list.add_in_tail(n4)
        list.add_in_tail(n5)
        node=list.find(3)
        self.assertIsNotNone(node)
        self.assertEqual(3,node.value)
        self.assertEqual(list.tail,None)

    def When_ListNotContainsValue_Find_MustReturnNone(self):
        list=LinkedList2()
        n1=Node(1)
        n2=Node(2)
        n3=Node(3)
        n4=Node(4)
        n5=Node(5)
        n1.next=n2
        n2.prev=n1
        n2.next=n3
        n3.prev=n2
        n3.next=n4
        n4.prev=n3
        n4.next=n5
        n5.prev=n4
        list.add_in_tail(n1)
        list.add_in_tail(n2)
        list.add_in_tail(n3)
        list.add_in_tail(n4)
        list.add_in_tail(n5)
        node=list.find(-2)
        self.assertIsNone(node)

    def When_ListNotContainsValue_FindAll_MustReturnEmptyList(self):
        list=LinkedList2()
        n1=Node(1)
        n2=Node(1)
        n3=Node(2)
        n4=Node(2)
        n5=Node(2)
        n1.next=n2
        n2.prev=n1
        n2.next=n3
        n3.prev=n2
        n3.next=n4
        n4.prev=n3
        n4.next=n5
        n5.prev=n4
        list.add_in_tail(n1)
        list.add_in_tail(n2)
        list.add_in_tail(n3)
        list.add_in_tail(n4)
        list.add_in_tail(n5)
        collection=list.find_all(-1)
        self.assertEqual(collection==[],True)

    def When_ListContainsValuesFromHead_FindAll_MustReturnCorrectElements(self):
        list=LinkedList2()
        n1=Node(1)
        n2=Node(1)
        n3=Node(1)
        n4=Node(1)
        n5=Node(2)
        n1.next=n2
        n2.prev=n1
        n2.next=n3
        n3.prev=n2
        n3.next=n4
        n4.prev=n3
        n4.next=n5
        n5.prev=n4
        list.add_in_tail(n1)
        list.add_in_tail(n2)
        list.add_in_tail(n3)
        list.add_in_tail(n4)
        list.add_in_tail(n5)
        collection=list.find_all(1)
        self.assertEqual(collection==[1,1,1,1],True)

    def When_ListContainsValuesFromTail_FindAll_MustReturnCorrectElements(self):
        list=LinkedList2()
        n1=Node(2)
        n2=Node(1)
        n3=Node(1)
        n4=Node(1)
        n5=Node(1)
        n1.next=n2
        n2.prev=n1
        n2.next=n3
        n3.prev=n2
        n3.next=n4
        n4.prev=n3
        n4.next=n5
        n5.prev=n4
        list.add_in_tail(n1)
        list.add_in_tail(n2)
        list.add_in_tail(n3)
        list.add_in_tail(n4)
        list.add_in_tail(n5)
        collection=list.find_all(1)
        self.assertEqual(collection==[1,1,1,1],True)

    def When_ListContainsValuesFromMiddle_FindAll_MustReturnCorrectElements(self):
        list=LinkedList2()
        n1=Node(2)
        n2=Node(1)
        n3=Node(1)
        n4=Node(1)
        n5=Node(2)
        n1.next=n2
        n2.prev=n1
        n2.next=n3
        n3.prev=n2
        n3.next=n4
        n4.prev=n3
        n4.next=n5
        n5.prev=n4
        list.add_in_tail(n1)
        list.add_in_tail(n2)
        list.add_in_tail(n3)
        list.add_in_tail(n4)
        list.add_in_tail(n5)
        collection=list.find_all(1)
        self.assertEqual(collection==[1,1,1],True)

    def When_ListEmpty_Delete_Must_BeCorrect(self):
        list=LinkedList2()
        n1=Node(2)
        list.delete(n1.value)
        self.assertEqual(list.len(),0)
        self.assertEqual(list.head,None)
        self.assertEqual(list.tail,None)

    def When_ListIsNotEmpty_Delete_HeadMustChangeHead(self):
        list=LinkedList2()
        n1=Node(1)
        n2=Node(2)
        n3=Node(3)
        n4=Node(4)
        n5=Node(5)
        n1.next=n2
        n2.prev=n1
        n2.next=n3
        n3.prev=n2
        n3.next=n4
        n4.prev=n3
        n4.next=n5
        n5.prev=n4
        list.add_in_tail(n1)
        list.add_in_tail(n2)
        list.add_in_tail(n3)
        list.add_in_tail(n4)
        list.add_in_tail(n5)
        list.delete(n1.value)
        self.assertEqual(list.len(),4)
        self.assertEqual(list.head.value,2)
        self.assertEqual(list.tail.value,5)

    def When_ListIsNotEmpty_Delete_FromTail_Must_ChangeListTail(self):
        list=LinkedList2()
        n1=Node(1)
        n2=Node(2)
        n3=Node(3)
        n4=Node(4)
        n5=Node(5)
        n1.next=n2
        n2.prev=n1
        n2.next=n3
        n3.prev=n2
        n3.next=n4
        n4.prev=n3
        n4.next=n5
        n5.prev=n4
        list.add_in_tail(n1)
        list.add_in_tail(n2)
        list.add_in_tail(n3)
        list.add_in_tail(n4)
        list.add_in_tail(n5)
        list.delete(n5.value)
        self.assertEqual(list.len(),4)
        self.assertEqual(list.head.value,1)
        self.assertEqual(list.tail.value,4)

    def When_ListIsNotEmpty_Delete_FromMiddle_Must_ChangeList(self):
        list=LinkedList2()
        n1=Node(1)
        n2=Node(2)
        n3=Node(3)
        n4=Node(4)
        n5=Node(5)
        n1.next=n2
        n2.prev=n1
        n2.next=n3
        n3.prev=n2
        n3.next=n4
        n4.prev=n3
        n4.next=n5
        n5.prev=n4
        list.add_in_tail(n1)
        list.add_in_tail(n2)
        list.add_in_tail(n3)
        list.add_in_tail(n4)
        list.add_in_tail(n5)
        list.delete(n3.value)
        self.assertEqual(list.len(),4)
        self.assertEqual(list.head.next.next.value,4)
        self.assertEqual(list.tail.prev.prev.value,2)



if __name__ == '__main__':
       unittest.main()

