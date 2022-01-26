"""
I used class variables for tracking instead of a list cause we're 
not tracking particular parking spots (although in an actual garage ofc we'd want that)
use of ParkingGarage demoed below, just run to see its effects

There were some other features I'd like to have added-- time tracking, income
tracking, etc., but my feeble attempts fell flat. 

ISSUES:
-'PayforParking' doesn't work-- I'm still not sure how to deal with class variables without
putting everything in the __init__ method which would be a lot

"""

class ParkingGarage():
    current_ticket = {"paid":False}
    taken_spaces = []
    taken_tix = []

    def __init__(self, name, spaces, tickets):
        self.name=name
        self.spaces = spaces
        self.tickets = tickets
    
    def takeTik(self):
        x = self.spaces.pop(0)
        self.taken_tix.append(x)

        y = self.tickets.pop(0)
        self.taken_tix.append(y)

        tik_num = len(self.spaces)
        print(f"Here is ticket number {y}.")
        print(f"There are {tik_num} spaces left.")

    '''
    not using an input variable cause i. Brandon said I can set the price
    and ii. I can't run the input in VS code so I can't demo it 
    ''' 

    #this function doesn't work
    def payForParking(self):
        x = input("Please enter your ticket number.")
        if x not in self.spaces:
            print(f"That will be ${x}.")
            print("Your ticket has been paid! You have 15mins to leave.")
            self.current_ticket["paid"] = True
        elif x in self.taken_spaces:
            print("You're here illegally. The police are on their way.")

    def leaveGarage(self):
        if self.current_ticket["paid"] == True:
            print("Thank you, have a nice day!")
        elif self.current_ticket["paid"] == False:
            x = input("Please pay! What's your ticket number?")
            print(f"great, that will be {x} dollars.")

            self.spaces.append(x)
            self.tickets.append(x)

#creating the first instance
temple_garage = ParkingGarage("Temple Garage",[1,2,3,4,5,6,7,8,9,10],[1,2,3,4,5,6,7,8,9,10])
print(temple_garage.spaces)
print(temple_garage.name)

#testing the Taketik method 
temple_garage.takeTik()
print(temple_garage.spaces)

#testing the payForParking method 
print(temple_garage.taken_tix)
temple_garage.payForParking()

#testing the leaveGargae method
temple_garage.leaveGarage()
print(temple_garage.daily_income)

