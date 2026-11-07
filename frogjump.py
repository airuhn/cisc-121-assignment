def solution(X, Y, D):

    distance = Y - X
    jumps = distance // D

    # if there is a remainder, we need to add one more jump
    if distance % D != 0:

        jumps += 1

    return jumps