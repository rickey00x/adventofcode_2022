tail_X = 0	
tail_Y = 0
head_X = 0
head_Y = 0
viseted = set()
viseted.add((0,0))

with open('Day9\Input.txt') as f:
    lines = f.read().split("\n")
    for line in lines:
        dicret,count = line.split(' ')
        for i in range(int(count)):
            if dicret == 'R':
                head_X += 1
            elif dicret == 'L':
                head_X -= 1
            elif dicret == 'U':
                head_Y += 1
            elif dicret == 'D':
                head_Y -= 1
            if not ((abs(head_X - tail_X) <= 1) and (abs(head_Y - tail_Y)) <= 1):
                if head_X > tail_X:
                    tail_X += 1
                elif head_X < tail_X:
                    tail_X -= 1
                if head_Y > tail_Y:
                    tail_Y += 1
                elif head_Y < tail_Y:   
                    tail_Y -= 1   
                viseted.add((tail_X,tail_Y))
    print(len(viseted))

           
            