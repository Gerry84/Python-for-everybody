#10.2
try:
    fhand = open('mbox-short.txt')
except:
    print("Can't open the file")
    exit()

d = dict()
for lines in fhand:
    words = lines.split()
    if len(words) == 0 or words[0] != 'From': continue
    else:
        time = words[5]
        epos = time.find(':')
        hour = time[0:epos]
        for count in hour:
            d[hour] = d.get(hour,0) + 1

l = list()
for key, val in d.items():
    l.append((key, val))
l.sort()
for i, e in l:
    print(i, e)
