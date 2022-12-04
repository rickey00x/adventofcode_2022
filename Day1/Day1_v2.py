with open('Day1/Input.txt') as f:
    maxcal =0
    secondmaxcal = 0
    thirdmaxcal = 0
    cals = 0
    for line in f:
        if line.strip():
            cals += int(line.replace("\n", ""))
        else:
            if cals > maxcal:
                thirdmaxcal = secondmaxcal
                secondmaxcal = maxcal
                maxcal = cals
            elif cals > secondmaxcal:
                thirdmaxcal = secondmaxcal
                secondmaxcal = cals
            elif cals > thirdmaxcal:
                thirdmaxcal = cals
            cals = 0
    print((maxcal+secondmaxcal+thirdmaxcal))


