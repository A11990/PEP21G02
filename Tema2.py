"""Homework 2 - needs to be presented before exam day"""

# 20P
# 1) Prove that "and" operation takes precedence over "or" operation by setting
# parentheses in the following expression (False or False and True or True)

# 40P
# 2) Get from input two different times in the format dd:hh:mm:ss and print the difference between them in the
# received format dd:hh:mm:ss
# dd is number of days
# hh is number of hours (00-23)
# mm is number od minutes (00-59)
# ss is number of seconds (00-59)

# 40P
# Calculate the diagonal of a rectangle with sides lenght recievd from input
#p1
print((False or False and True or True))
print((False or False) and (True or True))
print((False or (False and True) or True))
#p2
x = input('Get date1:')
days = x[0:2]
hours = x[3:5]
minutes = x[6:8]
seconds = x[9:11]

y = input("Get date2: ")

days2 = y[0:2]
hours2 = y[3:5]
minutes2 = y[6:8]
seconds2 = y[9:11]

t1 = int(days*24*hours+3600*hours+60*minutes+60*seconds)
t2 = int(days2*24*hours2+3600*hours2+60*minutes2+60*seconds2)
tf = t1 - t2
print('The diference is:', tf)
#p3
import math
L = int(input("Enter Length: "))
w = int(input("Enter Width: "))
diagonal =round(math.sqrt((w*2) + (L*2)))
print("Diagonal is: ", diagonal)