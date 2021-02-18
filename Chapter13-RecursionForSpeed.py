# -*- coding: utf-8 -*-
#!/usr/bin/python
#Chapter13
#Q1: sort in python has efficiency as O(N*logN)
def highestInThree(arr):
    arr = sorted(arr)
    l = len(arr) - 1
    return arr[l] * arr[l-1] * arr[l-2]
array3 = [11,8,3,4,5,6,7,8,9,10]
print(highestInThree(array3))

#Q2:
def findMissingNumber(arr):
    arr = sorted(arr)
    for i in range(0, len(arr)):
        if i != arr[i]:
            return i
array4 =  [9, 3, 2, 5, 6, 7, 1, 0, 4]
print(findMissingNumber(array4))

#Q3:Bubble sort as O(N^2) method, Quicksort as O(NlogN) and
#    insertion sort as O(N^2/2)
array3 = [11,8,3,4,5,6,7,8,9,10]
def findGreatestNumber1(arr):
    for i in range(0, len(arr)-1):
        if arr[i] < arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr[0]

print(findGreatestNumber1(array3))

def findGreatestNumber2(arr):
    arr = sorted(arr)
    return arr[len(arr) - 1]
print(findGreatestNumber2(array3))

def findGreatestNumber3(arr):
    for i in range(1, len(arr)):
        j = i - 1
        for j in range(0, i):
            while arr[j] > arr[i]:
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = arr[i]
        print(j)
    return arr[len(arr)-1]
print(findGreatestNumber3(array3))
