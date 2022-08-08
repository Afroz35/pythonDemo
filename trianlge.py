pass
class Train:
    def __init__(self,name,fare,seats):
        self.name=name
        self.fare=fare
        self.seats=seats

    def getStatus(self):
        print("..............")
        print(f"\nTrain Name:{self.name}")
        print(f"Seats available in train are {self.seats}")
        print("..............")
    def fareInfo(self):
        print(f"The price of a single ticket:{self.fare}")
    def bookTicket(self):
        if(self.seats>0):
            print(f"your ticket has been successfully booked\nYour seat number is{self.seats}")
            self.seats-=1
        else:
            print("Sorry tickets are not available")
    def CancelTicket(self,seatNo):
        pass
obj=Train(input("Name of train:"),int(input("Fare")),int(input("No of seats")))
obj.getStatus()
obj.bookTicket()