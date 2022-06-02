# take user input for the index position
# print out number at that index position


# userIndex is the end of the range?


#if userIndex == fib1  or userIndex == fib3  or userIndex == fib5:
#    print(userIndex)
# doesnt work as userIndex is an index not the actuall value!


#  list of fib sequence
fibList = [0,0,1,1,2,3,5,8,13]


# fib logic function
def fibo():
    #  get user input
    userIndex = input("\tWhat index do you want to view?")

    
    if userIndex == 0 or userIndex == 1:
        print("\tThe number at that position is 0")
    else:
        while userIndex > len(fibList):
            newVal = fibList[-1]+ fibList[-2]
            fibList.append(newVal)
        print("\tThe number at %d position is %d" % userIndex, fibList[-1])