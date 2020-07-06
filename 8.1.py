#8.1.
list = []
try:
    fhand = open('romeo.txt')
    for lines in fhand:
        line = lines.rstrip()
        words = line.split()
        for word in words:
            if word not in list:
                list.append(word)
            else: continue
except:
    print('File not found')
list.sort()
print(list)
