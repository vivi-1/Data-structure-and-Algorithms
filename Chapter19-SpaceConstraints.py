# -*- coding: utf-8 -*-
#!/usr/bin/python
#Chapter19 Q3
def reverse(arr):
    len1 = len(arr)
    for i in range(0, int(len1/2)):
            arr[i], arr[len1-1-i] = arr[len1-1-i], arr[i]

arr4 = ['a', 'b', 'c', 'd', 'c', 'e']
reverse(arr4)
print(arr4)
