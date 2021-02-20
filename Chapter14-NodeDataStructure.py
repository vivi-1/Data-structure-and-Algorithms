# -*- coding: utf-8 -*-
#!/usr/bin/python
#Chapter14
#Q1:
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    def print_LinkList(self):
        current = self.head
        while current:
            print (current.data)
            current = current.next
    def insert(self, data):
        new_node = Node(data)
        if(self.head):
            current = self.head
            while(current.next):
                current = current.next
            current.next = new_node
        else:
            self.head = new_node

list1 = LinkedList()
list1.insert("Wei")
list1.insert("Wang")
list1.insert("Kevin")
list1.insert("Yu")

list1.print_LinkList()
