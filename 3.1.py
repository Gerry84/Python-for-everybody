#3.1
hours = input('Enter number of hours: ')
rate = input('Enter rate: ')
if int(hours) - 40 <= 0:
    pay = int(hours) * int(rate)
else:
    pay = 40 * int(rate) + (int(hours)-40) * 1.5 * int(rate)
print('Pay: ',pay)
