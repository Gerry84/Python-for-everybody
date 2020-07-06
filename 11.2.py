#11.2
import re
try:
    fhand = open('mbox-short.txt')
except:
    print("Can't open file")
    exit()

count = 0
total = 0
l = list()
for lines in fhand:
    lines = lines.rstrip()
    revision = re.findall('New Revision:.([0-9.]+)', lines)
    if len(revision) > 0:
        for num in revision:
            total = total + int(num)
            count = count + 1
#        total = total + int(revision)


print(total/count)
