#10.1
d = dict()
try:
    fhand = open('mbox-short.txt')
except:
    print("Can't find file")
    exit()

for lines in fhand:
    words = lines.split()
    if len(words) == 0 or words[0] != 'From': continue
    else:
        mail = words[1]
        d[mail] = d.get(mail,0) + 1
#print(d)

l = list()
for key, val in d.items():
    l.append((val,key))
l.sort(reverse=True)

res = list()
for key, val in l:
    res.append((val, key))

print(res[0])
