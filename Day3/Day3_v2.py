def compare(lines):
    for i in range(len(max(lines, key=len))):
        if (lines[1].find(lines[0][i]) > -1) and (lines[2].find(lines[0][i]) > -1):
            return lines[0][i]
    print ('Invalid input'+lines[0]+lines[1]+lines[2])

def calcvalue(a):
    if a.isupper():
        return(ord(a) - ord('A') + 27)
    else:
        return(ord(a) - ord('a') + 1)
    
with open('Day3\Input.txt') as f:
    sum = 0
    lines= []
    for line in f:
        lines.append(line)
        if len(lines) >= 3:
                    sum = sum + calcvalue(compare(lines))
                    lines = []
    if len(lines) > 0:
        print ('err')
    print (sum)