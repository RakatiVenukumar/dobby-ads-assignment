# no of days in a month in a particular year using functions

def days_in_month(year,b):
    if b == '2':
        if year%400 == 0 or year%100 != 0 and year%4==0:
            print("The year is leap year and no of days are 29")
        else:
            print("The year is not a leap year and no of days are 28")
    elif b == '1' or b =='3' or b =='5' or b == '7' or b == '8' or b == '10' or b == '12':
        print("The no of days in this month are 31")
    elif b == '4' or b == '6' or b == '9' or b == '11':
        print("The no of days in this month are 30")

days_in_month(2022,'9')

