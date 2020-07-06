#9.1
d = dict()
try:
    fhand = open('mbox-short.txt')
except:
    print("Can't open file")
    exit()

for lines in fhand:
    if not lines.startswith('From'): continue
    elif lines.startswith('From:'): continue
    else:
        line = lines.rstrip()
        words = line.split()
        date = words[2]
        d[date] = d.get(date,0) + 1

print(d)
