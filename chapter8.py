#!/usr/bin/python

#Q1:
arrlib1 = {1: True, 2: True, 3: True, 4: True, 5: True}
def intersection(arr):
    result = []
    for x in arr:
        if arrlib1[x] == True:
            result.append(x)
    print (result)
arr1 = [0, 2, 4, 6, 8]
intersection(arr1)

#Q2:
arrlib2 = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f':0}
arrlib_temp
def fdup(arr):
    for x in arr:
        arrlib2[x] += 1
        if arrlib2[x] > 1:
            print(x)
            break
arr2 = ['a', 'b', 'c', 'd', 'c', 'e', 'f']
fdup(arr2)

#Q3:
arrlib3 = {'a':True, 'b':True, 'c':True, 'd':True, 'e':True, 'f':True, 'h':True, 'i':True, 'j':True, 'k':True, 'l':True, 'm':True, 'n':True, 'o':True, 'p':True, 'q':True, 'r':True, 's':True, 't':True, 'u':True, 'v':True, 'w':True, 'x':True, 'y':True, 'z':True}
def fmiss(str):
    result = []
    for x in str:
        if arrlib3[x] != True:
            result.append(x)
    print (result)
str1 = "the quick brown box jumps over a lazy dog"
fmiss(str1)

#Q4:
arrlib4 = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'h':0, 'i':0, 'j':0, 'k':0, 'l':0, 'm':0, 'n':0, 'o':0, 'p':0, 'q':0, 'r':0, 's':0, 't':0, 'u':0, 'v':0, 'w':0, 'x':0, 'y':0, 'z':0}
def fndup(str):
    for x in str:
        arrlib4[x] += 1
    for x in str:
        if arrlib4[x] == 1:
            print (x)
            break
str2 = "minimum"
fndup(str2)
