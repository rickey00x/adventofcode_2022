with open('Day4\Input.txt') as f:
    sum = 0
    for line in f:
        line =line.replace("\n", "")
        firstelf, secondelf = line.split(',')
        firstelf_start, firstelf_end = firstelf.split('-')
        secondelf_start, secondelf_end = secondelf.split('-')
        firstelf_start = int(firstelf_start)
        firstelf_end = int(firstelf_end)
        secondelf_start = int(secondelf_start)
        secondelf_end = int(secondelf_end)

        if(firstelf_start >= secondelf_start and firstelf_end <= secondelf_end):
                sum += 1
        elif(secondelf_start >= firstelf_start and secondelf_end <= firstelf_end):
                sum += 1  
    print (sum)