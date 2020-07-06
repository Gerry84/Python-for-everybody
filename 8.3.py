#8.3

list = []
while True:
    number = input('Please enter a number: ')
    if number == 'done': break
    else:
        try:
            number = int(number)
            list.append(number)
        except:
            print('Bad number')
print(max(list),min(list))
