# -*- coding: utf-8 -*-
#!/usr/bin/python
#Chapter11
#Q1:
def s_len(arr):
    if len(arr) == 1:
        return len(arr[0])
    return len(arr[0]) + s_len(arr[1: ])
inp = ["ab", "c", "def", "ghij"]
print (s_len(inp))


#Q2:
def piceven(arr):
    if len(arr) == 0:
        return []
    else:
        if (arr[0] % 2) == 0:
            return arr[0:1] + piceven(arr[1:len(arr)])
        else:
            return piceven(arr[1:len(arr)])
array2 = [1,2,3,4,5,6,7,8,9,10]
print(piceven(array2))

#Q3:
def tranN(n):
    if n==1:
        return 1
    else:
        return n + tranN(n-1)

print(tranN(6))

#Q4:
def xindex(str):
    if len(str) == 1:
        return 0
    else:
        if str[0] == 'x':
            return 0
        else:
            return 1 + xindex(str[1:len(str)])
print(xindex("abcdefghijklmnopqrstuvwxyz"))


#Q5:
def shortway(r, c):
    if r == 0 or c == 0:
        print ("r=0=c")
        return 0
    if r == 1 == c:
        return 0
    if c == 1 and r != 1:
        return 1 + shortway(r-1, 1)
    if r == 1 and c != 1:
        return 1 + shortway(1, c-1)
    if c > 1 and r > 1:
        print ("r=1")
        print(shortway(r-1, c-1))
        return 2 + shortway(r-1, c-1)


print(shortway(3, 3))
