import calendar

yy = 2019
mm = 8

#To ask month and year from the user:
yy = int(input("Enter year: "))
mm = int(input("Enter month: "))

#Displays the calendar
print("\n\n" + calendar.month(yy,mm))
