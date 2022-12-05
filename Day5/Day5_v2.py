stack = [[]]

def move(command):
    idx = command[1]-1
    new = command[2]-1
    for i in range(command[0],0,-1):
        if stack[idx]:
            length = len(stack[idx])
            if i <= length:
                a = stack[idx][length-i]
                stack[idx].pop(length-i)
                stack[new].append(a) 

with open('Day5\Input.txt') as f:
    first, second = f.read().split('\n\n')
# First part
for lines in reversed(first.splitlines()):
    for i in range(0, len(lines), 4):
        if(lines[i+1].isnumeric()):
            stack.append([])
        elif lines[i+1] != ' ':
            stack[int(i/4)].append(lines[i+1])
# Second part
for lines in second.splitlines():
    command = [int(s) for s in lines.split() if s.isdigit()]
    move(command)

for i in range(0, len(stack)-1):
    print(stack[i][-1],end = '')