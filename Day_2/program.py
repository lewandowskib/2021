file = open("input2.txt", "r")
content = file.read().replace(' ', '')
test = content.split('\n')
depth = 0
horizontal = 0
aim = 0
for element in test:
    if "forward" in element:
        horizontal += int(element[-1])
        depth += aim * int(element[-1])

    if "down" in element:
        #depth += int(element[-1])
        aim += int(element[-1])

    if "up" in element:
        # depth -= int(element[-1])
        aim -= int(element[-1])

print("Result is", horizontal*depth)
