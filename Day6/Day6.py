
def find_dup_char(input):
    x=[]
    for i in input:
        if i not in x and input.count(i)>1:
            return True


with open('Day6\Input.txt') as f:
    length = 14
    text = f.read()
    for i in range(0, len(text)):
        if(not find_dup_char(text[i:i+length])):  
            print(i+14)
            break