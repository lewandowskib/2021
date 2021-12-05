
file = open("input.txt", "r")
content = file.read()
test = content.split('\n')
result = []
revers_result = []
one = 0
zero = 0

for lenght in range(0, 13):
    if one > zero:
        result.append("1")
    if one < zero:
        result.append("0")
    one = 0
    zero = 0
    if lenght == 12:
        pass
    else:
        for i in test:
            if i[lenght] == "1":
                one += 1
            if i[lenght] == "0":
                zero += 1

for i in result:
    if i == "1":
        revers_result.append("0")
    if i == "0":
        revers_result.append("1")

print("Result is", int("".join(result), 2)*int("".join(revers_result), 2))
