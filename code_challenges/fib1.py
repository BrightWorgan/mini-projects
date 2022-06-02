# take user input for the index position
# print out number at that index position


# list of Fibonacci sequence
fibList = [0,0,1]

# fib logic function
def fibo(userIndex):
    if userIndex == 0 or userIndex == 1:
        print("\tThe number at that position is 0")
    else:
        while userIndex > len(fibList)-2:
            newVal = fibList[-1]+ fibList[-2]
            fibList.append(newVal)
        print("\tThe number at %d position is %d" % (userIndex, fibList[-1]))
