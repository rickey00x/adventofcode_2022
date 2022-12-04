def calculate( x , y ):	
    if (y == 'X'):
        if(x == 'A'):
            return 4
        elif(x == 'B'):
            return 1
        elif(x == 'C'):
            return 7
    elif ( y == 'Y'):	
        if(x == 'A'):
            return 8
        elif(x == 'B'):
            return 5
        elif(x == 'C'):
            return 2
    elif ( y == 'Z'):	
        if(x == 'A'):
            return 3
        elif(x == 'B'):
            return 9
        elif(x == 'C'):
            return 6
    else:
        print ('Invalid input'+x+y)

result = 0
with open('Day2\Input.txt') as f:
    for line in f:
        x, y = line.split(' ')
        result += calculate(x, y[0])
print (result)







