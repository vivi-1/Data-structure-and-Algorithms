# -*- coding: utf-8 -*-
#!/usr/bin/python
#Chapter10 Q4
def print_mix(arr):
    for i in arr:
        if isinstance(i, int) == True:
            print (i)
        else:
            print_mix(i)
array = [1,2,3,[4, 5, 6], 7,[8,[9, 10, 11,[12, 13, 14]]],[15, 16, 17, 18, 19,[20, 21, 22,[23, 24, 25,[26, 27, 29]], 30, 31], 32], 33]
print_mix(array)
