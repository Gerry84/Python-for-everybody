#4.1
def computepay(hours, rate):
    if hours < 40:
        pay = hours * rate
        print('Pay: ',pay)
    else:
        pay = 40 * rate + (hours - 40) * 1.5 * rate
        print('Pay: ',pay)

try:
    hours = input('Enter number of hours: ')
    hours = float(hours)
    rate = input('Enter rate: ')
    rate = float(rate)
    computepay(hours, rate)
except:
    print('Error, enter numeric numbers')
