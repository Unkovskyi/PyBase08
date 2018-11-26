#Task 1

name=input('Input your name ')
surname=input('Input your surname ')
print('Hello ',name,surname)
print('---------------------')
in_date=int(input('Input date of birthday from 0 to 31: '))
in_month=int(input('Input month of birthday from 1 to 12: '))
in_year=int(input('Input year of birthday max 2018: '))
print('---------------------')

cur_year=2018
cur_month=11
cur_date=19

cur_days=(cur_year-1)*360+(cur_month-1)*30+cur_date
in_days=(in_year-1)*360+(in_month-1)*30+in_date

age_y=cur_year-in_year
print ('Your age as of 19.11.2018 is',age_y,'year(-s)')

age_m=int((cur_days-in_days)/30)
print ('Your age as of 19.11.2018 is',age_m,'month')

age_d=cur_days-in_days
print('Your age as of 19.11.2018 is ',age_d, 'day(-s)')

print('Your age as of 19.11.2018 is {} days {} month {} years'.format(age_d%360,age_m%12,age_y))