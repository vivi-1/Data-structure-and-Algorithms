# -*- coding: utf-8 -*-
#!/usr/bin/python
#Chapter20 Q1



#Q2:
def missingNum(arr):
    HT = {}
    min = arr[0]
    max = arr[0]
    for i in range(0,len(arr)):
        if arr[i] > max:
            max = arr[i]
        if arr[i] < min:
            min = arr[i]
        HT[arr[i]] = 1
    for i in range (min, max):
        if i not in HT.keys():
            return i
arr5 = [2, 3, 0, 6, 1, 5]
print(missingNum(arr5))
