#9.3.
d = dict()
try:
    fhand = open('mbox-short.txt')
except:
    print("Can't open file")
    exit()

for lines in fhand:
    words = lines.split()
    if len(words) == 0 or words[0] != 'From': continue
    else:
        mail = words[1]
        d[mail] = d.get(mail, 0) + 1

max = None
for key in d:
    if max is None or max < d[key]:
        max = d[key]
        mail = key

print(mail, max)
