def solution(A):
    unpaired = set()

    for number in A:
        if number in unpaired:
            # remove the number from the set when its pair is found
            unpaired.remove(number)
        else:
            unpaired.add(number)

    # return the values that are left without a pair
    return unpaired.pop()
