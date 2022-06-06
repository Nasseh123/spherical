from datetime import date,datetime, timedelta,time

from dateutil.relativedelta import *


def gettime(number_of_months):  #NUMBER OF MONTH CAN BE A NEGATIVE NUMBER OR POSITIVE NUNMBER
    date = datetime.today()
    # print(date)
    # 2018-09-24 13:24:04.007620

    date2 = date + relativedelta(months=number_of_months)
    first_day  = date2 +relativedelta(day=1)
    last_day = date2 + relativedelta(day=31)
    # print(date22)
    # print(date3)
    data = {
        'first_day': datetime.combine(first_day, time.min),
        'last_day':datetime.combine(date, time.max),
    }
    return data
