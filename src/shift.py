from datetime import datetime, timedelta


class Shift:

    def __init__(self, date):
        self.date = date
        self.start_time = ""
        self.end_time = ""
        self.title = ""

    def get_length(self):
        time_1 = datetime.strptime(self.start_time, "%H:%M:%S")
        time_2 = datetime.strptime(self.end_time, "%H:%M:%S")

        if time_2.hour == 0:
            time_2 = datetime(time_2.year, time_2.month, time_2.day+1, time_2.hour, time_2.minute, time_2.second)

        time_interval = time_2 - time_1
        return time_interval

    def add_start(self, start_time):
        """

        :param start_time: '18:30'
        """
        self.start_time = start_time + ":00"

    def add_end(self, end_time):
        """

        :param end_time: '18:30'
        """
        self.end_time = end_time + ":00"

    def add_title(self, title):
        self.title = title


    def __str__(self):
        return "shift done in "+str(self.date)+" from: "+str(self.start_time)+" until: "+str(self.end_time)+" it lasted = "+str(self.get_length()) + " worked as: " + self.title

    def __repr__(self):
        return "{},{},{},{},{}".format(self.date, self.start_time, self.end_time, self.get_length(), self.title)


# shift = Shift("12/12/12")
# shift.add_start("18:30")
# shift.add_end("23:30")
# print(shift)





