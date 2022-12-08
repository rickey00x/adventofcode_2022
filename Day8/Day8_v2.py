map = []

def check_left(x,y):
    for i in range(y-1,-1,-1):
        if map[x][i]>= map[x][y]:
            return y-i
    return y

def check_right(x,y):
    for i in range(y+1,len(map[x])):
        if map[x][i]>= map[x][y]:
            return i-y
    return len(map[x])-y-1

def check_up(x,y):
    for i in range(x-1,-1,-1):
        if map[i][y]>= map[x][y]:
            return x-i
    return x

def check_down(x,y):
    for i in range(x+1,len(map)):
        if map[i][y]>= map[x][y]:
            return i-x
    return len(map)-x-1

def eval():
    maxview = 0
    for i in range(0,len(map)):
        for j in range(0,len(map[i])):
            view = check_left(i,j)*check_right(i,j)*check_up(i,j)*check_down(i,j)
            if view > maxview:
                maxview = view            
    print(maxview)        
   
with open('Day8\Input.txt') as f:
    lines = f.read().split("\n")
    for line in lines:
        map.append(list(line))
    eval()