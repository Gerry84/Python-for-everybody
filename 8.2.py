#8.2.
list = []
try:
    fhand = open('mbox-short.txt')
    for lines in fhand:
        if lines.startswith('From:'): continue
        elif not lines.startswith('From'): continue
        else:
            line = lines.rstrip()
            lines.split()
            words = lines.split()
            list.append(words[1])
except:
    print('File not found')

count = 0
for l in list:
    print(l)
    count = count + 1

print('There were %d lines in the file with From as the first word' % (count))
