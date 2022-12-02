# calorie intake
# numbers separted by a whitespace
# add up each elf's daily calories and then sort higher to lower, print out highest

calorieList = [[1000, 2000, 3000, 4000], [5000, 6000], [7000, 8000, 9000], [10000]]
# calorieList = ["1000 2000 3000 4000", "5000 6000", "7000 8000 9000", "10000"]
addedCalories = []
count = []


# for item in calorieList:
#     for i in calorieList[int(i)]:
#         count.append(i)
#         addedCalories.append(count)
# print(addedCalories)

# for item in calorieList:
#     calorieList[i][i]

for item in calorieList:
    for i in range(0, len(item)):
        count += i
addedCalories.append(count)