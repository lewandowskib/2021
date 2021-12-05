file = open("input3.txt", "r")
content = file.read()
test = content.split('\n')

result = []
tab_test = []
for count in range(0, 12):
    one = 0
    zero = 0
    for number in test:
        if int(number[count]) == 1:
            one += 1
        else:
            zero += 1

    if one >= zero:
        value = '1'
    else:
        value = '0'
    for element in test:
        if int(element[count]) != int(value):
            test.remove(element)

print(test)
