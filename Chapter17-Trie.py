# -*- coding: utf-8 -*-
#!/usr/bin/python
#Chapter17
#Q3 Q4:
class TrieNode:
    def __init__(self, char):
        self.char = char
        self.end = False
        self.counter = 0
        self.children = {}
class Trie(object):
    def __init__(self):
        self.root = TrieNode("")
    def insert(self, word):
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                newNode = TrieNode(char)
                node.children[char] = newNode
                node = newNode
        node.children['*'] = None
        node.end = True
        node.counter += 1
    def traverse(self, node):
        for char in node.children:
            print(char)
            if char != '*':
                self.traverse(node.children[char])
    def collection(self, node = None, word="", words=[]):
        currentNode = node or self.root
        for key in currentNode.children:
            if key == '*':
                words.append(word)
            else:
                self.collection(node.children[key], word+key, words)
        return words
    def autocorrection(self, word):
        node = self.root
        temp = ""
        for char in word:
            if char in node.children:
                node = node.children[char]
                temp += char
            else:
                return temp + self.collection(node, "", [])[0]
        return word

list3 = Trie()
list3.insert("wang")
list3.insert("Wei")
list3.insert("yu")
list3.insert("kevin")
list3.insert("want")
list3.insert("weight")

#list3.traverse(list3.root)

print(list3.autocorrection("kw"))
