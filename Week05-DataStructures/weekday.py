#Author: https://pynative.com/python-get-the-day-of-week/#:~:text=isoweekday()%20to%20get%20a%20weekday%20of%20a%20given%20date%20in%20Python,-The%20weekday()&text=Use%20the%20isoweekday()%20method,in%20place%20of%20weekday()%20.&text=The%20output%20is%201%2C%20which,Monday%20as%20Monday%20is%201.
#I altered an already available code to get the result.
#I first began by trying to define each number as a day i.e. 1 = Monday
#Then If it was monday -friday for it to say itt was a weekday.
#I discovered it was much more compact and easier to do if left as an integer.


import datetime

x_date = datetime.date(2022, 4, 22)
no = x_date.weekday()

if no < 5:
    print("Yes, unfortunately today is a weekday.")

else:  
    print("It is the weekend, yay!")