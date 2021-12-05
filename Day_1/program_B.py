file = open("input.txt", "r")
content = file.read()
test = content.split('\n')
tab = []
increased = 0

for i in range(len(test)-3):
    tab.append(int(test[i]) + int(test[i+1]) + int(test[i+2]))


for j in range(len(tab)-1):
    if tab[j] < tab[j+1]:
        increased += 1
    print(increased)
