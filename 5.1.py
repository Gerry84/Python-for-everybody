#5.1
count = 0
total = 0
while True:
    number = input('Enter a number: ')
    if number == 'done': break
    try:
        number = int(number)
        count = count + 1
        total = total + number
    except:
        print('Bad data')
        continue
print('Total: ',total)
print('Count: ',count)
average = total / count
print('Average: ',average)
