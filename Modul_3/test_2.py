from datetime import datetime, time, date, timedelta

import parse


#
# from datetime import timedelta
# d = timedelta(microseconds=-1)
# (d.days, d.seconds, d.microseconds)
# print(d)


# def dt1(year, month, day):
#     dt = datetime.date(2017, 4, 20)
#     return print(dt)
#
#
# dt1(2017, 4, 20)

aaa = datetime.strptime('12:13:14', '%H:%M:%S')
print(aaa)

