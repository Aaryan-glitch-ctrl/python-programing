from datetime import date
date1 =(1,5,2016)
date2 =(1,5,2022)

d1 = date(date1[2],date1[1],date1[0])
d2 = date(date2[2],date2[1],date2[0])

days_between = abs((d2-d1).days)

print("Number of days between dates:", days_between)


