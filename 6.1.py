#6.1
str = 'X-DSPAM-Confidence:0.8475'
stpoint = str.find(':')
stpoint = int(stpoint)
print(stpoint)
length = len(str)
print(length)
number = str[stpoint+1:length]
number = float(number)
print(number)
