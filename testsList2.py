import unittest
from LinkedListTwoWay import *

class Test_testsList2(unittest.TestCase):
    
    def test_When_ListIsEmpty_Len_Should_BeZero(self):
        list=LinkedList2()
        self.assertEqual(list.len(),0)

    def test_When_ListIsNotEmptyAndHasFiveElements_Len_Should_ProvideFiveValue(self):
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

    def test_When_ListIsEmpty_AddInHead_MustBeAdded(self):
        list=LinkedList2()
        n1=Node(1)
        list.add_in_head(n1)
        self.assertEqual(list.len(),1)
        self.assertEqual(list.head.value,1)

    def test_When_ListIsNotEmpty_AddInHead_MustChangeCurrentHead(self):
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
        self.assertEqual(list.head.value,100)

    def test_When_ListIsEmpty_Clean_MustMakeListAllEmpty(self):
        list=LinkedList2()
        list.clean()
        self.assertEqual(list.len(),0)
        self.assertEqual(list.head,None)
        self.assertEqual(list.tail,None)

    def test_When_ListIsNotEmpty_Clean_MustMakeListEmpty(self):
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

    def test_When_ListContainsValue_Find_MustReturnItem(self):
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

    def test_When_ListNotContainsValue_Find_MustReturnNone(self):
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

    def test_When_ListNotContainsValue_FindAll_MustReturnEmptyList(self):
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

    def test_When_ListContainsValuesFromHead_FindAll_MustReturnCorrectElements(self):
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
        self.assertEqual(collection==[n1,n2,n3,n4],True)

    def test_When_ListContainsValuesFromTail_FindAll_MustReturnCorrectElements(self):
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
        self.assertEqual(collection==[n2,n3,n4,n5],True)

    def test_When_ListContainsValuesFromMiddle_FindAll_MustReturnCorrectElements(self):
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
        self.assertEqual(collection==[n2,n3,n4],True)

    def test_When_ListEmpty_Delete_Must_BeCorrect(self):
        list=LinkedList2()
        n1=Node(2)
        list.delete(n1.value)
        self.assertEqual(list.len(),0)
        self.assertEqual(list.head,None)
        self.assertEqual(list.tail,None)

    def test_When_ListIsNotEmpty_Delete_HeadMustChangeHead(self):
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

    def test_When_ListIsNotEmpty_Delete_FromTail_Must_ChangeListTail(self):
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

    def test_When_ListIsNotEmpty_Delete_FromMiddle_Must_ChangeList(self):
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

    def test_When_ListHasOnlyOneElement_Delete_MustCleanList(self):
        list=LinkedList2()
        n1=Node(1)
        list.add_in_tail(n1)
        list.delete(n1.value)
        self.assertEqual(list.len(),0)
        self.assertEqual(list.head,None)
        self.assertEqual(list.tail,None)

    def test_When_ListHasSeveralItemsInMiddle_DeleteAll_MustDeleteAllItemsByValue(self):
        list=LinkedList2()
        n1=Node(1)
        n2=Node(2)
        n3=Node(2)
        n4=Node(2)
        n5=Node(3)
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
        list.delete(2,True)
        self.assertEqual(2,list.len())
        self.assertEqual(list.head.next,n5)
        self.assertEqual(list.tail.prev,n1)

    def test_When_ListHasServeralItemsFromTail_DeleteAll_MustDeleteAllItemsByValueFromHead(self):
        list=LinkedList2()
        n1=Node(2)
        n2=Node(2)
        n3=Node(2)
        n4=Node(3)
        n5=Node(3)
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
        list.delete(3,True)
        self.assertEqual(3,list.len())
        self.assertEqual(list.head,n1)
        self.assertEqual(list.tail,n3)

    def test_When_ListAllItemsEqualValue_DeleteAll_MustMakeListClean(self):
        list=LinkedList2()
        n1=Node(3)
        n2=Node(3)
        n3=Node(3)
        n4=Node(3)
        n5=Node(3)
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
        list.delete(3,True)
        self.assertEqual(0,list.len())
        self.assertEqual(list.head,None)
        self.assertEqual(list.tail,None)

    def test_When_ListHasNoNodesEqualValue_DeleteAll_MustNotChangeList(self):
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
        list.delete(6,True)
        self.assertEqual(5,list.len())
        self.assertEqual(list.head,n1)
        self.assertEqual(list.tail,n5)

    def test_When_ListHasNoNodesEqualValue_Delete_MustNotChangeList(self):
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
        list.delete(6)
        self.assertEqual(5,list.len())
        self.assertEqual(list.head,n1)
        self.assertEqual(list.tail,n5)

    def test_When_ListIsEmpty_DeleteAll_MustBeCorrect(self):
        list=LinkedList2()
        list.delete(6)
        self.assertEqual(0,list.len())
        self.assertEqual(list.head,None)
        self.assertEqual(list.tail,None)

    def test_When_ListHasOnlyOneElementEqualToValue_DeleteAll_MustMakeListEmpty(self):
        list=LinkedList2()
        n1=Node(1)
        list.add_in_tail(n1)
        list.delete(n1.value,True)
        self.assertEqual(0,list.len())
        self.assertEqual(list.head,None)
        self.assertEqual(list.tail,None)

    def test_When_ListIsNotEmpty_InsertAfterHead_MustInsertNode(self):
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
        newNode=Node(100)
        list.insert(n1,newNode)
        self.assertEqual(6,list.len())
        self.assertEqual(list.head.next,newNode)
        self.assertEqual(list.head.next.next,n2)

    def test_When_ListIsNotEmpty_InsertInMiddle_MustInserNode(self):
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
        newNode=Node(100)
        list.insert(n3,newNode)
        self.assertEqual(6,list.len())
        self.assertEqual(list.head.next.next.next,newNode)
        self.assertEqual(list.tail.prev.prev,newNode)

    def test_When_ListIsNotEmpty_InsertInTail_MustInsertNode(self):
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
        newNode=Node(100)
        list.insert(n5,newNode)
        self.assertEqual(6,list.len())
        self.assertEqual(list.tail,newNode)
        self.assertEqual(list.tail.prev,n5)

    def test_When_AfterNodeIsNoneAndListIsNotEmpty_Must_AddInTail(self):
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
        newNode=Node(100)
        list.insert(None,newNode)
        self.assertEqual(6,list.len())
        self.assertEqual(list.head,n1)
        self.assertEqual(list.tail,newNode)

    def test_When_NewNodeIsNone_Must_NotChangeList(self):
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
        newNode=Node(100)
        list.insert(n3,None)
        self.assertEqual(5,list.len())
        self.assertEqual(list.head,n1)
        self.assertEqual(list.tail,n5)

    def test_When_AfterNodeIsNotExistsInList_Must_NotChangeList(self):
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
        newNode=Node(100)
        afterNode=Node(9)
        list.insert(afterNode,newNode)
        self.assertEqual(5,list.len())
        self.assertEqual(list.head,n1)
        self.assertEqual(list.tail,n5)

    def test_When_ListIsEmptyAndAfterNodeIsNone_Must_AddNewNodeInHead(self):
        list=LinkedList2()
        newNode=Node(100)
        list.insert(None,newNode)
        self.assertEqual(1,list.len())
        self.assertEqual(list.head,newNode)
        self.assertEqual(list.tail,newNode)


if __name__ == '__main__':
    unittest.main()
