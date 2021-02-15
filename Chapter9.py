# -*- coding: utf-8 -*-
#!/usr/bin/python
#Chapter 9 Q4
def rev(str):
    temp1 = []
    temp2 = []
    for x in str:
        temp1.append(x)
    for i in range(0, len(str)):
        temp2.append(temp1.pop())
    print(temp2)
word = "abcde"
rev(word)
