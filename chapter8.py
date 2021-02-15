# -*- coding: utf-8 -*-
#!/usr/bin/python

#Q1:
def intersection(arr1, arr2):
    arrlib = {}
    result = []
    for x in arr1:
        arrlib[x] = True
    for y in arr2:
        if y in arrlib.keys():
            result.append(y)
    print (result)
arr1 = {0, 2, 4, 6, 8}
arr2 = {1, 2, 3, 4, 5}
intersection(arr1, arr2)

#Q2:
def fdup(arr):
    arrlib = {}
    for x in arr:
        if x in arrlib.keys():
            print(x)
            break
        else:
            arrlib[x] = True

arr3 = ['a', 'b', 'c', 'd', 'c', 'e', 'f']
fdup(arr3)



#Q3:
arrlib3 = {'a':True, 'b':True, 'c':True, 'd':True, 'e':True, 'f':True, 'h':True, 'i':True, 'j':True, 'k':True, 'l':True, 'm':True, 'n':True, 'o':True, 'p':True, 'q':True, 'r':True, 's':True, 't':True, 'u':True, 'v':True, 'w':True, 'x':True, 'y':True, 'z':True}
def fmiss(str):
    result = []
    arrlib= {}
    str1 = "abcdefghijklmnopqrstuvwxyz"
    for x in str:
        arrlib[x] = True
    for y in str1:
        if arrlib.get(y) is None:
            result.append(y)
    print (result)
str1 = "the quick brown box jumps over a lazy dog"
fmiss(str1)

#Q4:
def fndup(str):
    arrlib = {}
    for x in str:
        arrlib[x] = 0
        arrlib[x] += 1
    for x in str:
        if arrlib[x] == 1:
            print (x)
            break
str2 = "minimum"
fndup(str2)
