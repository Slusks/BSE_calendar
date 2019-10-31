import datetime
from datetime import date, timedelta
import pprint

import Scheduling



new_date = '2019-09-28' #input('What weekend are we adding?')
idiot = 'Tricanowicz' # input('who are we giving it too')
for i in Scheduling.shift_list:
    print(i.saturday)
    if new_date in str(i.saturday):
        i.coverage = idiot
        days = [i.saturday.strftime('%b %d %Y'), i.sunday.strftime('%b %d %Y')]
        Scheduling.Tricanowicz.weekends.append(days)
    elif new_date in str(i.sunday):
        i.coverage = idiot
        days = list[i.saturday.strftime('%b %d %Y'), i.sunday.strftime('%b %d %Y')]
        Scheduling.Tricanowicz.weekends.append(days)
    else:
        print('this isnt a real date')



print(Scheduling.Tricanowicz.weekends)
print(Scheduling.shift_list)