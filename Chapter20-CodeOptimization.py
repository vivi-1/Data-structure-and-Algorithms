# -*- coding: utf-8 -*-
#!/usr/bin/python
#Chapter20

#Q1:

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

#Q3:

#Q4:
def maxProduct(arr):
    if len(arr) <= 1:
        return arr[0]
    if len(arr) == 2:
        return arr[1]*arr[0]
    largestPos = 0
    secondLargPos = 0
    posCnt = 0
    leastMin = 0
    secondLeastMin = 0
    minCnt = 0
    zeroCnt = 0
    for i in range(0,len(arr)):
        if arr[i] > 0:
            if arr[i] > largestPos:
                secondLargPos = largestPos
                largestPos = arr[i]
            if arr[i] < largestPos and arr[i] > secondLargPos:
                secondLargPos = arr[i]
            posCnt += 1
        if arr[i] < 0:
            if arr[i] < leastMin:
                secondLeastMin = leastMin
                leastMin = arr[i]
            if arr[i] > leastMin and arr[i] < secondLeastMin:
                secondLeastMin = arr[i]
            minCnt += 1
        if arr[i] ==0:
            zeroCnt += 1

    if posCnt >=2 and minCnt >= 2:
        return max(largestPos*secondLargPos, leastMin*secondLeastMin)
    if posCnt <= 1 and minCnt >=2:
        return leastMin*secondLeastMin
    if posCnt >= 2 and minCnt <=1:
        return largestPos*secondLargPos
    if posCnt==1 and minCnt ==1 and zeroCnt >= 1:
        return 0

arr6 = [2, 3, 0, 6, 1, 5, -1, -2, -10]
arr7 = [2, -1, 0, 4, -10]
print(maxProduct(arr6))
print(maxProduct(arr7))
