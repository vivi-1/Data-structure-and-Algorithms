# -*- coding: utf-8 -*-
#!/usr/bin/python
#Chapter15
#Q3
class NodeTree:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    def insert(self, data):
        if self.data:
            if data <  self.data:
                if self.left == None:
                    self.left = NodeTree(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right == None:
                    self.right = NodeTree(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
    def treePrint(self):
        if self.left:
            self.left.treePrint()
        print(self.data)
        if self.right:
            self.right.treePrint()
    def printGreatestValue(node):
        if node.right == None:
            return node.data
        else:
            return node.right.printGreatestValue()

list2 = NodeTree(1)

list2.insert(2)
list2.insert(3)
list2.insert(4)
list2.insert(5)

list2.treePrint()
print(list2.printGreatestValue())
