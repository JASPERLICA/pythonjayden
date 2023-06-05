num_loops = 1
numbe = 1
star = "*"
space = " "


def part_of_tree():
    num = 1
    number = 1
    numbers = 16
    while num < 10:
        print (space*numbers + star*number)
        num = num + 1
        number = number + 2
        numbers = numbers - 1

while num_loops < 4:
    part_of_tree()
    num_loops = num_loops + 1

while numbe < 6:
    print (" "*15 + "***")
    numbe = numbe + 1

    
