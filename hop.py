__author__ = 'obscure'
import sys
'''
Given an array of integers where each element represents the max number of steps that can be made forward from that element. Write a function to return the minimum number of jumps to reach the end of the array (starting from the first element). If an element is 0, then cannot move through that element.

Example:

Input: arr[] = {1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9}
Output: 3 (1-> 3 -> 8 ->9)
First element is 1, so can only go to 3. Second element is 3, so can make at most 3 steps eg to 5 or 8 or 9.'''

a = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
res = []

for i in range(len(a)):
    res.append(sys.maxsize-9)
print(len(a))
res[len(a)-1] = 0

for i in range(len(a)-2,-1,-1):
    for j in range(i+1, len(a)):
        if a[i]+i >= j :#j is reachable ?
            if res[i] > res[j] + 1:
                res[i] = res[j] + 1
print(res)