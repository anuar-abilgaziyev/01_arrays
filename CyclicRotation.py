# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K):
    size = len(A)
    if size == 0:
        return A
    K = K % size
    result = []
    result.extend(A[-K:])
    result.extend(A[:-K])
    return result