'''
Rotation of the array means that each element is shifted right by one index, 
and the last element of the array is moved to the first place. 

For example, the rotation of array A = [3, 8, 9, 7, 6] is [6, 3, 8, 9, 7] 
(elements are shifted right by one index and 6 is moved to the first place).
'''

def solution(A, K):
    size = len(A)
    if size == 0:
        return A
    K = K % size
    result = []
    result.extend(A[-K:])
    result.extend(A[:-K])
    return result
