# -*- coding: utf-8 -*-
#!/usr/bin/python
#Chapter14
#Q1, Q3, Q4
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
    def insert_end(self, data):
        new_node = Node(data)
        if(self.head):
            current = self.head
            while(current.next):
                current = current.next
            current.next = new_node
        else:
            self.head = new_node
            return
    def print_lastelement(self):
        current = self.head
        while current.next:
            current = current.next
        print(current.data)
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
            if next:
                next = next.next
        self.head = prev
    def delete_mid(self, node):
        next = node.next
        while node.next:
            node.data = next.data
            node = next
        node = None

list1 = LinkedList()
e1 = Node("Kevin")
list1.insert_end("Wei")
list1.insert_end("Wang")
list1.insert_end(e1)
list1.insert_end("Yu")

list1.print_LinkList()
list1.print_lastelement()

list1.reverse()
list1.print_LinkList()

list1.delete_mid(e1)
list1.print_LinkList()

#Q2:
class Node2:
    def __init__(self, data=None, next=None, prev = None):
        self.data = data
        self.prev = prev
        self.next = next
class DoublyLinkedList:
    def __init__(self):
        self.head = None
    def print_LinkList(self):
        current = self.head
        while current:
            print (current.data)
            current = current.next
    def append(self, data):
        new_node = Node2(data)
        new_node.next = None
        if(self.head):
            current = self.head
            while(current.next):
                current = current.next
            current.next = new_node
            new_node.prev = current
        else:
            new_node.prev = None
            self.head = new_node
            return
