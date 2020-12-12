# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

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