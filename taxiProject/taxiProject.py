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

# list of question names
listOfQuestions = ["q1", "q2", "q3", "q4","q5"]

# get taxi id/ reg. number using userInput
userInput = input("\tPlease enter the reg number of the taxi: ").lower()


# check if taxt id/reg. number is alrady in the database
if userInput in dic:
    print("\tTaxi all ready exists, \n\t TEST Statement")
    # update nested dict.
    # questionSeeker()

else:
    dic['taxiID2345E'] = {"q1":"3", "q2" : "3", "q3" : "1", "q4" : "3", "q5" : "n"}
    # for loop


# if present update

# if not present create new entry
dic['taxiID2345E'] = {"q1":"3","q2" : "3","q3" : "1","q4" : "3","q5" : "n"}

# five quries
# add number to taxi's dictionalry
# calculate new average 
# if updated average is below 12 generate email E1 or if nameOfQuestion is yes gernerate email E2

# taxi class
class Taxi :

    # class init
    def __init__(self, num = "", cleanRating = 0, serviceRating = 0, commRating = 0, drivingRating = 0 ):
        # num
        if num == None or if len(newnum) != len(11):
            raise Exception ("\t*** A Vaild Taxi Number is necessary ***")
        self.__num = num

        # q1 cleanliness 
        if type(cleanRating) == int and cleanRating > 0 and cleanRating <= 5:
            self.__rating = cleanRating
        else:
            raise Exception("*** Invaid Rating!*** Rating must be from 1-5")

        # q2 General customer service
        if type(serviceRating) == int and serviceRating > 0 and serviceRating <= 5:
            self.__rating = serviceRating
        else:
            raise Exception("*** Invaid Rating!*** Rating must be from 1-5")
        
        # q3 Communication
        if type(commRating) == int and commRating > 0 and commRating <= 5:
            self.__rating = commRating
        else:
            raise Exception("*** Invaid Rating!*** Rating must be from 1-5")

        # q4 Driving competency
        if type(drivingRating) == int and drivingRating > 0 and drivingRating <= 5:
            self.__rating = drivingRating
        else:
            raise Exception("*** Invaid Rating!*** Rating must be from 1-5")

# class functions
    def addTaxi(self):
        newnum = (input("\t Please provide a Taxi ID Number: "))
        if len(newnum) != len(11):
            print("\tPlease Enter an eleven character")
            return
        newnum = int(newnum)