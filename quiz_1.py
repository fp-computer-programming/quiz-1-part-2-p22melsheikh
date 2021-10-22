# Author: MEE 10/22/21

y = int(input("Enter the year of the date  "))
q = int(input("Enter the day of the date:  "))
m = int(input("Enter the month of the date: "))

j = y / 100
k = y % 100

if m == 1:
    m == str("January")
if m == 2: 
    m == str("February")

h = (q + ((26 * (m+1))//10) + k + (k/4) + (j/4) + (5*j)) % 7

if h == 0:
    h = str("Saturday")
    elif h == 1:
        h = str("Sunday")
    elif h == 2:
        h = str("Monday")
    elif h == 3:
        h = str("Tuesday")
    elif h == 4: 
        h = str("Wednesday")
    elif h == 5:
        h = str("Thursday")
    elif h == 6:
        h = str("Friday")



print("The day was a " + str(h))






 


