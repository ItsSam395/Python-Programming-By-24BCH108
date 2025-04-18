from datetime import datetime

date1_input = input("Enter the first date (day,month,year): ")
day1, month1, year1 = [int(x) for x in date1_input.split(',')]
date1 = datetime(year1, month1, day1)

date2_input = input("Enter the second date (day,month,year): ")
day2, month2, year2 = [int(x) for x in date2_input.split(',')]
date2 = datetime(year2, month2, day2)

difference = abs((date2 - date1).days)
print("Number of days between the two dates:", difference)
