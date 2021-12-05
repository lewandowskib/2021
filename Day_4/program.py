import random

file = open("input1.txt", "r")
content = file.read()
test = content.split('\n')
bingo_numbers = []
bingo_boards = []
for line in test:
    if line == test[0]:
        bingo_numbers = line.split(",")
    else:
        if line == "":
            continue
        else:
            bingo_boards.append(line.split(" "))

drawn_bingo_numbers = 0
run = True

while run:
    bingo_number = bingo_numbers[drawn_bingo_numbers]
    for i in bingo_boards:
        for element in i:
            if bingo_number == element:
                i[i.index(element)] = "\033[1m" + element + "\033[0m"
    if drawn_bingo_numbers >= 3:
        for i in bingo_boards:
            bold_numbers = 0
            for element in i:
                if "\033[1m" in element:
                    bold_numbers += 1
                if bold_numbers == 5:
                    print(" ".join(i))
                    print("Numer ostatni to: ", bingo_number)
                    print(bingo_boards.index(i))
                    run = False

    drawn_bingo_numbers += 1

exit()
for ass in bingo_boards:
    print(" ". join(ass))
