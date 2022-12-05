# Advent Code Challanenge Day 1: Elf Calorie Intake 

# numbers separted by a whitespace
# Plan: add up each elf's daily calories and then sort higher to lower, print out highest

calorieList = []
# test list 
# calorieList = [[1000, 2000, 3000, 4000], [5000, 6000], [7000, 8000, 9000], [10000]]

# open txt file
f = open("./adventOfCodeChallenges/day1/day1Cals.txt", "r")
temp = f.readlines()

# for loop to create each Elf's caloire intake
smallArray = []
for item in temp:
    if item != "\n" :
        smallArray.append(int(item))
    else:
        calorieList.append(smallArray)
        smallArray = []

# close file
f.close() 

# print(calorieList)

# addedCalories = []
# count = 0

# for elf in calorieList:
#     for calories in elf:
#         count += calories
#     addedCalories.append(count)
#     count = 0
# print(addedCalories)

# # printing highest cal
# fatElf = addedCalories[0]
# for elf in addedCalories:
#     if elf > fatElf:
#         fatElf = elf
# else: print("\tThe elf with the highest calorie intake is ", fatElf)

addedCalories = []
count = 0

for elf in calorieList:
    for calories in elf:
        count += calories
    addedCalories.append(count)
    count = 0

addedCalories.sort(reverse=True)
print(addedCalories)

# top three elves i.e those with the highest snack/ calorie amounts
no1Elf = addedCalories[0]
no2Elf = addedCalories[1]
no3Elf = addedCalories[2]

#
print("\t No. 1 Elf is %d, No.2 Elf is %d and the Elf in third place is %d" % (no1Elf , no2Elf , no3Elf))
# total amount of calories in the top three
print("\t The top three Elves have a total amount of caloreis of ", (no1Elf + no2Elf + no3Elf ))
