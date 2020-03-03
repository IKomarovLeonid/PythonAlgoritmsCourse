class Node:

    def __init__(self, v):
        self.value = v
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node != None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        node=self.head
        list=[]
        while node is not None:
            if node.value==val:
                list.append(node)
            node=node.next
        return list

    def delete(self, val, all=False):
        target=self.find(val)
        if target is None:
           pass
        else:
            if all is False:
                node=self.head
                prev=None
                while node is not None:
                    if node.value is val:
                        if prev is None:
                            self.head=self.head.next
                            pass
                        else:
                            prev.next=node.next
                            pass
                    prev=node
                    node=node.next
            else:
               temp=self.head
               prev=None
               while temp is not None:
                   if  temp.value is val:
                       if prev is None:
                           self.head=self.head.next                          
                       else:
                           prev.next= temp.next                         
                   prev= temp
                   temp= temp.next
        pass
                


    def clean(self):
        self.head=None
        self.tail=None
        pass 

    def len(self):
        count=0;
        node=self.head
        while node is not None:
            count=count+1
            node=node.next
        return count 

    def insert(self, afterNode, newNode):
        nAfter=self.find(afterNode.value)
        if nAfter is None:
            pass
        else: 
            if afterNode is self.tail:
                afterNode.next=newNode
                pass
            else: 
                newNode.next=afterNode.next
                afterNode.next=newNode
                pass
        pass 

