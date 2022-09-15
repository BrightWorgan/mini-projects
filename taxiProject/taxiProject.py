# dictionary to temp store data
dic = {
    "taxiID1234D": {
        "q1":"3",
        "q2" : "3",
        "q3" : "1",
        "q4" : "3",
        "q5" : "n"
        },
          "taxiID10002F": {
        "q1":"1",
        "q2" : "1",
        "q3" : "1",
        "q4" : "1",
        "q5" : "n"
        },
}

# get taxi id/ reg. number
# userInput

userInput = input("\tHi there\n\t Thank you for choosing to use GoTaxi\n\tPlease enter the reg number of the taxi: ").lower()


# check if taxt id/reg. number is alrady in the database
if userInput in dic:
    pass
else:
    dic['taxiID2345E'] = {"q1":"3","q2" : "3","q3" : "1","q4" : "3","q5" : "n"}

# if present update

# if not present create new entry
dic['taxiID2345E'] = {"q1":"3","q2" : "3","q3" : "1","q4" : "3","q5" : "n"}

# five quries

# 1 cleanliness

# 2 General customer service

# 3 Communication

# 4 Driving competency

# 5 yes / no question
qwertty = input("\tDid the diver refuse service?\n y/n?\n").lower()

# add number to taxi's dictionalry

# calculate new average 

# if updated average is below 12 generate email E1 or if nameOfQuestion is yes gernerate email E2
