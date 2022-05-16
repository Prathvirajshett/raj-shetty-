
class Train:
    def __init__(self,seat,fare) :
        self.seat=seat
        self.fare=fare
    def bookTickets(self):
        self.seats=-1
    def getStatus(self):
        print(self.seats)
    def getFareInfo(self):
        print(self.fare)
    
tr= Train(78,175)
tr.bookTickets()
tr.getStatus()
tr.getFareInfo()
tr.getStatus()