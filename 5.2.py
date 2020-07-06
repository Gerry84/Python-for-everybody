#5.2.
max = None
min = None
while True:
    number = input('Enter number: ')
    try:
        if number == 'done': break
        number = int(number)
        if max is None or number > max:
            max = number
        if min is None or number < min:
            min = number
        else: continue
    except:
        print('Bad number')
        continue
print('Max: ',max)
print('Min: ',min)
