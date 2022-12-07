from collections import defaultdict
cwd = []
siezes = defaultdict(int)


with open('Day7\Input.txt') as f:
    lines = f.read().split("\n")
    for line in lines:
        input = line.split(' ')
        if input[0] == '$':
            input.remove(input[0])
            if input[0] == "cd":
                input.remove(input[0])
                if input[0] == "..":
                    cwd.pop()
                elif input[0] == "/":
                    cwd = []
                elif input[0].isalpha():
                    cwd.append(input[0])            
                else:
                    print("Invalid input", input[0])
        else:
            if input[0].isnumeric():
                for i in range (0, len(cwd)+1):
                    siezes['/'.join(cwd[:i])] += int(input[0])

sum = 0
for key, value in siezes.items():
    if value <= 100000:
        sum += value
print(sum)     















