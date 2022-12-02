# Advent Code Challanenge Day 1: Elf Calorie Intake 

# numbers separted by a whitespace
# Plan: add up each elf's daily calories and then sort higher to lower, print out highest

calorieList = [[1000, 2000, 3000, 4000], [5000, 6000], [7000, 8000, 9000], [10000]]
# calorieList = ["1000 2000 3000 4000", "5000 6000", "7000 8000 9000", "10000"]
# open txt file
f = open("day1Cals.txt", "r")
calorieList.append(f.readline())
f.close() 

print(calorieList)

addedCalories = []
count = 0

for elf in calorieList:
    for calories in elf:
        count += calories
    addedCalories.append(count)
    count = 0
print(addedCalories)

# printing highest cal
fatElf = addedCalories[0]
for elf in addedCalories:
    if elf > fatElf:
        fatElf = elf
else: print("The elf with the highest calorie intake is ", fatElf)