def compare(a, b):
    for i in range(len(a)):
        if b.find(a[i]) > -1:
            return a[i]
    print ('Invalid input'+a+b)

def calcvalue(a):
    if a.isupper():
        return(ord(a) - ord('A') + 27)
    else:
        return(ord(a) - ord('a') + 1)





with open('Day3\Input.txt') as f:
    sum = 0
    for line in f:
        line =line.replace("\n", "") #to remove the newline character
        x = len(line)
        a = line[0:x//2]
        b = line[x//2:x]
        sum += calcvalue(compare(a, b))
    print (sum)