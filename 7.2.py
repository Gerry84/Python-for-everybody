#7.2.
count = 0
total = 0
try:
    fhand = open('mbox-short.txt')
    for line in fhand:
        if line.find('X-DSPAM-Confidence') == -1: continue
        else:
            pos = line.find(':')
            epos = len(line)
            number = line[pos+2:epos]
            num = number.rstrip()
            print(num)
            count = count + 1
            total = total + float(num)
except:
    print('File not found')

print('Total Count: ', count)
print('Total number: ', total)
average = total / count
print(average)
