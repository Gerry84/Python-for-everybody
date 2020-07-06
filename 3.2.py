#3.2
hours = input('Enter number of hours: ')
rate = input('Enter rate: ')
try:
    if int(hours)<40:
        pay = int(hours) * int(rate)
        print('Pay: ',pay)
    else:
        pay = 40 * int(rate) + (int(hours)-40) * 1.5 * int(rate)
        print('Pay: ',pay)
except:
    print('Error, please enter numeric input')
