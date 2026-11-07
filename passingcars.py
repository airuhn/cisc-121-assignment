def solution(A):

    east_cars = 0
    passing = 0

    for car in A:
        if car == 0:    
            east_cars += 1
        else:
            # this car is traveling west, so it will pass all the cars that have traveled east
            passing+= east_cars

            # return -1 if the number of passing cars exceeds 1,000,000,000
            if passing > 1000000000:
                return -1


    return passing

