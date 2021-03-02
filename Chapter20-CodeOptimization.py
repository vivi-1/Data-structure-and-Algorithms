# -*- coding: utf-8 -*-
#!/usr/bin/python
#Chapter20

#Q1:
class Athelete:
    def __init__(self, first_name, last_name, team):
        self.first_name = first_name
        self.last_name = last_name
        self.team = team

def bothTeamPlayers(arr1, arr2):
    HT = {}
    result = []
    for i in arr1:
        HT[i.first_name + " " + i.last_name] = True
    for j in arr2:
        if (j.first_name + " " + j.last_name) in HT.keys():
            result.append(j.first_name + " " + j.last_name)
    return result

basketball_players = []
b1 = Athelete("Jill","Huang","Gators" )
b2 = Athelete("Janko", "Barton", "Sharks")
b3 = Athelete("Wanda", "Vakulskas", "Sharks")
b4 = Athelete("Jill", "Moloney","Gators")
b5 = Athelete( "Luuk","Watkins", "Gators")
basketball_players.append(b1)
basketball_players.append(b2)
basketball_players.append(b3)
basketball_players.append(b4)
basketball_players.append(b5)

football_players = []
f1 = Athelete("Hanzla","Radosti","32ers")
f2 = Athelete("Tina", "Watkins", "Barleycorns")
f3 = Athelete("Alex", "Patel", "32ers")
f4 = Athelete("Jill", "Huang", "Barleycorns")
f5 = Athelete("Wanda", "Vakulskas", "Barleycorns")
football_players.append(f1)
football_players.append(f2)
football_players.append(f3)
football_players.append(f4)
football_players.append(f5)
print(bothTeamPlayers(basketball_players, football_players))

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
def is_increase(arr, i, j):
    for k in range(i,j):
        if arr[k+1] < arr[k]:
            return False
    return True


def maxProfit(arr):
    buy_price = arr[0]
    profit = 0

    for price in arr:
        temp_profit = price - buy_price
        if price < buy_price:
            buy_price = price
        if temp_profit > profit:
            profit = temp_profit
    return profit

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

#Q5:
import numpy as np
def sortTemp(arr):
    HT={}
    for i in np.linspace(97,99,21,endpoint=True):
        HT[i] = []
    for j in arr:
        HT[j].append(j)
    arr = []
    for k, v in HT.items():
        if v != []:
            arr += v
    return arr

tempreture = [98.6, 98.0, 97.1, 99.0, 98.9, 97.8, 98.5, 98.2, 98.0, 97.1]
print(sortTemp(tempreture))

#Q6:
def longestConsecutiveLen(arr):
    HT={}
    largestCnt = 1
    for i in arr:
        HT[i] = True
    for i in arr:
        if i - 1 not in HT.keys():
            tempCnt = 1
            currentNum = i
            while currentNum +1 in HT.keys():
                currentNum += 1
                tempCnt += 1
            if tempCnt > largestCnt:
                largestCnt = tempCnt
    return largestCnt
arr8 = [19, 13, 15, 12, 18, 14, 17, 11]
arr9 = [10, 5, 12, 3, 55, 30, 4, 11, 2]
print(longestConsecutiveLen(arr8))
print(longestConsecutiveLen(arr9))
