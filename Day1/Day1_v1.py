with open('Day1/Input.txt') as f:
    maxcal =0
    cals = 0
    for line in f:
        if line.strip():
            cals += int(line.replace("\n", ""))
        else:
            if cals > maxcal:
                maxcal = cals
            cals = 0
    print(maxcal)


