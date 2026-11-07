def solution(A, K):
    if len(A) == 0:
        return A

    for i in range(K):

        # move the last element to the front of the list

        last_element = A.pop()  
        A.insert(0, last_element) 

    return A

print(solution([3, 8, 9, 7, 6], 3))