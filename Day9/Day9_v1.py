tail_X = 0	
tail_Y = 0
head_X = 0
head_Y = 0
visited = set()
visited.add((0,0))

with open('Day9\Input.txt') as f:
    lines = f.read().split("\n")
    for line in lines:
        direction,count = line.split(' ')
        for i in range(int(count)):
            if direction == 'R':
                head_X += 1
            elif direction == 'L':
                head_X -= 1
            elif direction == 'U':
                head_Y += 1
            elif direction == 'D':
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
                visited.add((tail_X,tail_Y))
    print(len(visited))

           
            