#!/usr/bin/ruby
#Chapter 12
#Q1:
def​ ​add_until_100​(array)
​ 	  ​return​ 0 ​if​ array.​length​ == 0
     sum_now = array[0] + add_until_100(array[1, array.​length​ - 1])
​ 	  ​if​ sum_now > 100
​ 	    ​return​ sum_now - array[0]
​ 	  ​else​
​ 	    ​return​ sum_now
​ 	  ​end​
​end​

#Q2:
def​ ​golomb​(n, memo = {})
​ 	  ​return​ 1 ​if​ n == 1
     if ! memo[n]
        memo[n] = 1 + golomb(n - golomb(golomb(n-1, memo), memo), memo)
     end
​ 	  ​return​ memo[n];
​​end​

#Q3:
def​ ​unique_paths​(rows, columns, memo{})
​ 	  ​return​ 1 ​if​ rows == 1 || columns == 1
     if !memo[[row, columns]]:
        memo[[row, columns]] = unique_paths(rows - 1, columns, memo) + unique_paths(rows, columns - 1, memo)
​ 	  ​end
    return​ memo[[row, columns]]
​​end​
