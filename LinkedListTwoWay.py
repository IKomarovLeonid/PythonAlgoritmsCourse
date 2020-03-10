class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class LinkedList2:  
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    def find(self, val):
        node=self.head
        while node is not None:
            if node.value==val:
                return node
            node=node.next
        return None

    def find_all(self, val):
        list=[]
        node=self.head
        while node is not None:
            if node.value==val:
                list.append(node)
            node=node.next
        return list

    def delete(self, val, all=False):
        node=self.find(val)
        if node is not None and all is True:
            tempNode=self.head
            while tempNode is not None:
                if tempNode.value is val:
                    self.delete(val)
                tempNode=tempNode.next
            return
        if node is not None and all is False:
            if node is self.head:
                if self.head.next is None:
                    self.head=None
                    self.tail=None
                    return
                else:
                    tempNode=self.head.next
                    tempNode.prev=None
                    self.head=tempNode
                    return
            if node is self.tail:
                self.tail=self.tail.prev
                self.tail.next=None
                return
            node.prev.next=node.next
            node.next.prev=node.prev
        return

    def clean(self):
        self.head=None
        self.tail=None
        pass

    def len(self):
        count=0
        node=self.head
        while node is not None:
            count=count+1
            node=node.next
        return count

    def insert(self, afterNode, newNode):
        if newNode is None: return
        if afterNode is None and self.len() == 0: 
            self.add_in_head(newNode)
            return
        if afterNode is None and self.len() != 0:
            self.add_in_tail(newNode)
            return

        node=self.find(afterNode.value)
        if node is not None:
            if node is self.tail:
                node.next=newNode
                newNode.prev=node
                self.tail=newNode
                return
            else:
                node.next.prev=newNode
                newNode.next=node.next
                newNode.prev=node
                node.next=newNode
                return
        return

    def add_in_head(self, newNode):
        if newNode is None: pass
        else:
            if self.head is None:
                self.head=newNode
                self.tail=newNode
                pass
            else:
                newNode.next=self.head
                self.head.prev=newNode
                self.head=newNode
                pass
