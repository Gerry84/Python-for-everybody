#11.1
import re
count = 0
x = input('Enter file name: ')
try:
    fhand = open(x)
except:
    print("Can't find file")
    exit()

expression = input('Enter regular expression: ')

for lines in fhand:
    lines = lines.rstrip()
    word = re.findall(expression, lines)
    if len(word) > 0:
        count = count + 1
print('%s had %d lines that matched %s' % (x, count, expression))
