
import random
import time
import datetime


class Employees(object):
    def __init__(self, my_info):
        for key in my_info:
            setattr(self, key, my_info[key])
# dictionary with information of employee
if __name__ == "__main__":
    my_info = {"Name": "Greg Baker",
                    "Age": "25",
                    "Position": "Sales Associate - Full time",
                    "Pay": "$17.00"}

result = Employees(my_info)

print(result.Name, result.Age, result.Position, result.Pay)


class Timecard():
    def __init__(self, clockIn, clockOut, submitTimeCard):
        self.clockIn = clockIn
        self.clockOut = clockOut
        self.submitTimeCard = submitTimeCard

print("WARNING: Time must be entered in 24 hour format")
# Clock in on timecard
clockIn = input("Enter start time in hours:min format: ")
# Clock out on timecard
clockOut = input("Enter end time in hours:min format: ")
# Submit timecard
submitTimeCard = input("Do you want to submit this time card? (y/n): ")
# Edit timecard

user = Timecard(clockIn, clockOut, submitTimeCard)


class WorkSchedule():

# Add which days of the week employee will work

# Request time off

class Paystubs():

# View paystubs

# Set up Direct Deposit
