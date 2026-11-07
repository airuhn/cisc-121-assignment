def solution(X, A):
    
    covered = set()

    for time in range(len(A)):
        position = A[time]
        covered.add(position)

        if len(covered) == X:
          return time

    # if the frog never reaches the other side, return -1
    return -1 

