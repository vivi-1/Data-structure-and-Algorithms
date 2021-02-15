#!/usr/bin/python3

#Q1:
arr1 = {1: True, 2: True, 3: True, 4: True, 5: True}
arr2 = [0, 2, 4, 6, 8]
result = []
for x in arr2:
    if arr1[x] == True:
        result.append(x)
print (result)

#Q2:
arrlib2 = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f':0}
arr2 = ['a', 'b', 'c', 'd', 'c', 'e', 'f']
for x in arr2:
    arrlib2[x] += 1
    if arrlib2[x] > 1:
      print(x)
      break
