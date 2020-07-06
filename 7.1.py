#7.1
try:
    fhand = open('mbox-short.txt')
    for line in fhand:
        text = line.upper()
        print(text)
except:
    print('File not found')
