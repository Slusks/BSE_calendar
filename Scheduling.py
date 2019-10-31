import datetime
from datetime import date, timedelta
import pprint



class Employee:
    def __init__(self, name, seniority, quota, shifts):
        self.name = name # first name. Class object name should be the employee's last name
        self.seniority = seniority #<- datetime object that is the employee's seniority date
        self.quota = quota #<- integer that stores how many weekends are covered
        self.weekends = list() # list object that lists the weekends covered

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.weekends

    def update_quota(self, shift_list): #this function updates the quota and cleans the dates
        for i in shift_list: #i is going to be a shift
            if self.name == i.coverage:
                days = [i.saturday.strftime('%b %d %Y'), i.sunday.strftime('%b %d %Y')]
                self.weekends.append(days)
            else:
                continue
        self.quota = len(self.weekends)
        #print(self.quota)


#( shift_list[x].coverage, ':', shift_list[x].saturday, 'to', shift_list[x].sunday,)

#create  a function that can iterate over a list to update the weekends attribute

class station:
    def __init__(self, name, engineer_week, engineer_weekend, dates, weekends):
        self.name = name #string
        self.engineer_week = engineer_week #required engineers per week
        self.engineer_weekend = engineer_weekend #required engineers per weekend
        self.dates =[] #dates the station is open by Monday-Sunday week
        self.weekends = weekends #integer that is the total number of weekends required at this station

        def __str__(self):
            return self.name



class Shift:
    def __init__(self, saturday, sunday, coverage, station):
        self.saturday = saturday
        self.sunday = sunday
        self.coverage = coverage

    def __str__(self):
        return self.coverage

Slusky = Employee('Sam', datetime.datetime(2015, 6, 9), 0, [])
Hagelgans = Employee('Adam', datetime.datetime(2015, 4, 13), 0, [])
Tricanowicz = Employee('Mike', datetime.datetime(2011, 7, 1), 0, [])
James = Employee('Emily', datetime.datetime(2015, 5, 20), 0, [])
Hogrefe = Employee('Colin', datetime.datetime(2015, 1, 5), 0, [])
Porter = Employee('Robb', datetime.datetime(2014, 12, 14), 0, [])
Bailey = Employee('Zach', datetime.datetime(2014, 1, 21), 0, [])
Greer = Employee('Josh', datetime.datetime(2012, 5, 23), 0, [])
Stedje = Employee('JohnS', datetime.datetime(2011, 10, 31), 0, [])
Haines = Employee('Jordan', datetime.datetime(2011, 3, 21), 0, [])
Cagle = Employee('JohnC', datetime.datetime(2010, 7,12), 0, [])
Malek = Employee('Devin', datetime.datetime(2005, 6, 13), 0, [])
Monyette = Employee('Tom', datetime.datetime(2004, 6, 1), 0, [])
Floren = Employee('Luis', datetime.datetime(1995, 8, 14), 0, [])


roster = [Slusky, James, Hagelgans, Hogrefe, Porter, Bailey, Greer, Stedje, Tricanowicz, Haines, Cagle, Malek, Monyette, Floren]




#print('roster len', len(roster))
def allsundays(year):
   d = date(year, 9, 1)                    # September first
   d += timedelta(days = 6 - d.weekday())  # First Sunday
   while d.year == year:
      yield d
      d += timedelta(days = 7)

def allsaturdays(year):
    sat = date(year, 9, 1)
    sat += timedelta(days = 5-sat.weekday())
    while sat.year == year:
        yield sat
        sat += timedelta(days = 7)

sunday_count = []
saturday_count = []
for d in allsundays(2019):
    sunday_count.append(d)
    #print(d)
#print( 'total sundays:', len(sunday_count)-1)

for sat in allsaturdays(2019):
    saturday_count.append(sat)
    #print(sat)
#print( 'total saturdays:', len(saturday_count)-1)

#print('len saturday', len(saturday_count))

########################This needs to be inside a function so it doesn't happen Every time
n = 0
shift_list =[]
for i,j in zip(saturday_count, sunday_count):
    if n < len(roster):
        shift_list.append(Shift(i, j, roster[n].name)) #just updating the name here to make a shift that is date, date, name
        n +=1
    elif n == len(roster):
        n = 0
        continue
########################### Above this needs to be in a function
pp = pprint.PrettyPrinter(indent = 4)
x = 0
for item in shift_list:
    #print(shift_list[x].coverage, ':', shift_list[x].saturday, 'to', shift_list[x].sunday,)
    x+=1

for emp in roster: #updates each employee's weekend coverage
    updating = Employee.update_quota(emp, shift_list)
    print(emp.name, ':', emp.weekends)

