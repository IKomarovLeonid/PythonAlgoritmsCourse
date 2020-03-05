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

        if self.len() != 0:
            node = self.head
            prev = None
            while node != None:
                if node.value == val:
                    if prev != None:
                        tmp = node.next
                        del(node)
                        prev.next = tmp
                        node = tmp
                        if tmp == None:
                            self.tail = prev
                    else:
                        tmp = node.next
                        del(node)
                        self.head = tmp
                        node = tmp
                        if tmp == None:
                            self.tail = tmp
                    if (all == False):
                        return
                else:
                    prev = node
                    node = node.next
        else:
            return

                

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

