#9.2
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
        d[mail] = d.get(mail,0) + 1

print(d)
