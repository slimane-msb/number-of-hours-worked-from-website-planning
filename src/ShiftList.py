import csv
from datetime import datetime

from src.shift import Shift

def get_hours_from_date(date):
    return

class ShiftList:

    def __init__(self):
        self.total = datetime.strptime("0:0:0", "%H:%M:%S")
        self.shifts = []

    def add_shift(self, shift):
        self.shifts.append(shift)
        self.total += shift.get_length()

    def remove_shift(self, shift):
        self.shifts.remove(shift)
        self.total -= shift.get_length

    def __str__(self):
        res = ""
        for shift in self.shifts:
            res += str(shift)+"\n"
        return res

    def __repr__(self):
        res = "{},{},{},{},{},{},{}\n".format("date", "start time", "end time", "duration","shift title","total time worked", "total hours worked")
        for shift in self.shifts:
            n_total = str(self.get_number_total()).split(",")
            res += shift.__repr__()+ ","+ n_total[0] + " and" + n_total[1] + "," +str(self.get_number_total_heur()) +"\n"
        return res

    def get_number_total(self):
        return self.total - datetime.strptime("0:0:0", "%H:%M:%S")

    def get_number_total_heur(self):
        total_date = self.get_number_total()
        return total_date.total_seconds()/60/60

    def save_in_csv(self):
        today = datetime.today()
        f = open(today.strftime("%Y%M%d%H%M%S")+".csv", "x")
        f.write(self.__repr__())
        f.close()





# probloems:
# get today and old oct, remove duplicates

#
# s1 = ShiftList()
#
# sh1 = Shift("12/12/2000")
# sh1.add_start("18:30")
# sh1.add_end("00:30")
# sh1.add_title("plange")
#
# sh2 = Shift("12/12/2001")
# sh2.add_start("19:30")
# sh2.add_end("00:30")
# sh2.add_title("plange")
#
# s1.add_shift(sh1)
# s1.add_shift(sh2)
# s1.add_shift(sh2)
# s1.add_shift(sh2)
# s1.add_shift(sh2)
#
# s1.add_shift(sh2)
# s1.add_shift(sh2)
# s1.add_shift(sh2)
# s1.add_shift(sh2)
#
# s1.add_shift(sh2)
# s1.add_shift(sh2)
# s1.add_shift(sh2)
# s1.add_shift(sh2)
#
# s1.add_shift(sh2)
# s1.add_shift(sh2)
# s1.add_shift(sh2)
# s1.add_shift(sh2)
#
# s1.add_shift(sh2)
# s1.add_shift(sh2)
# s1.add_shift(sh2)
# s1.add_shift(sh2)
#
# print(s1.__repr__())
# print(s1.get_number_total_heur())
# #
# s1.save_in_csv()







