map = []

def check_left(x,y):
    for i in range(y-1,-1,-1):
        if map[x][i]>= map[x][y]:
            return False
    return True 

def check_right(x,y):
    for i in range(y+1,len(map[x])):
        if map[x][i]>= map[x][y]:
            return False
    return True

def check_up(x,y):
    for i in range(x-1,-1,-1):
        if map[i][y]>= map[x][y]:
            return False
    return True

def check_down(x,y):
    for i in range(x+1,len(map)):
        if map[i][y]>= map[x][y]:
            return False
    return True

def eval():
    visable = 0
    for i in range(0,len(map)):
        for j in range(0,len(map[i])):
            if i == 0 or j == 0 or i == len(map)-1 or j == len(map[i])-1:
                visable += 1
            else:
                if(check_left(i,j)or check_right(i,j) or check_up(i,j) or check_down(i,j)):
                    visable += 1
    print(visable)        
   
with open('Day8\Input.txt') as f:
    lines = f.read().split("\n")
    for line in lines:
        map.append(list(line))
    eval()