import datetime
from datetime import timedelta, date
from datetime import datetime as dtm



#len(shift) = 10, the shift indices are 1-9
shift = ['SAT48', '11/23/20', '11/24/20', '11/25/20', '11/26/20', '11/27/20', '11/28/20', '11/29/20', '11/30/20', '12/01/20']
datetime_shift = []


days = len(shift)-1
#while days >= n > 0:
shift_dates = shift[1:days]
n = 1
for i in shift_dates:
    if n != days:
        date_string = i.split('/')
        print (date_string)
        date_obj = datetime.date(int('20'+date_string[2]), int(date_string[0]), int(date_string[1]))
        datetime_shift.append(date_obj)
        print(datetime_shift)
    elif n == days:
        datetime_shift.insert(0, shift[0])
        print (datetime_shift)



