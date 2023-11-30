from datetime import datetime

# Find how many days, weeks, month left if we want to live whatever age you want to live like 90 years in this case.
my_age=int(input('Enter Your Current Age:'))
wish_age=int(input('Enter Your Desire Death Age:'))

years_left=wish_age-my_age

days_left=int(years_left*365)

month_left=int(years_left*12)

week_left=int(days_left/7)


print(f'{years_left} Years \n{month_left}Months \n{week_left} Weeks\n{days_left} DAYS ')

