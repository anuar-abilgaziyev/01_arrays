'''
A non-empty array A consisting of N integers is given. 
The array contains an odd number of elements, 
and each element of the array can be paired with 
another element that has the same value, 
except for one element that is left unpaired.

The function, given an array A consisting of N integers fulfilling the above conditions, returns the value of the unpaired element.
'''

def solution(A):
    freq = {} 
    for num in A: 
        if (num in freq): 
            freq[num] += 1
        else: 
            freq[num] = 1
    
    for key, value in freq.items():
        if value % 2 == 1:
            return key
