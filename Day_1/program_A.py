file = open("input.txt", "r")
content = file.read()
test = content.split('\n')
result = 0

for i in range(len(test)):
    if test[i] > test[i-1]:
        result +=1
        print("increased")
    else:
        print("decreased")
    print("Result is", result)