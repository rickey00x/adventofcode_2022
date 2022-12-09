length = 10
X = []
Y = []
visited = set()
visited.add((0,0))

for i in range(length):
    X.append(0)
    Y.append(0)

with open('Day9\Input.txt') as f:
    lines = f.read().split("\n")
    for line in lines:
        direction,count = line.split(' ')
        for i in range(int(count)):
            if direction == 'R':
                X[0] += 1
            elif direction == 'L':
                X[0] -= 1
            elif direction == 'U':
                Y[0] += 1
            elif direction == 'D':
                Y[0] -= 1
            for j in range(1,len(X)):
                if not ((abs(X[j-1] - X[j]) <= 1) and (abs(Y[j-1] - Y[j])) <= 1):
                    if X[j-1] > X[j]:
                        X[j] += 1
                    elif X[j-1] < X[j]:
                        X[j] -= 1
                    if Y[j-1] > Y[j]:
                        Y[j] += 1
                    elif Y[j-1] < Y[j]:   
                        Y[j] -= 1   
                    if(j == len(X)-1):
                        visited.add((X[j],Y[j]))
                        
    print(len(visited))

           
            