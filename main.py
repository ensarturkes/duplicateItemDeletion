liste = [5, 10, 5, 8, 7, 1, 8, 5]
flag = 0
currentIndex = 0
print(liste)
while currentIndex < (len(liste)-1):
    i = currentIndex + 1
    while i < len(liste):
        if liste[currentIndex] == liste[i]:
            liste.pop(i)
            flag = 1
        else:
            i = i + 1
    if flag == 1:
        liste.pop(currentIndex)
        currentIndex = -1
        flag = 0
    currentIndex = currentIndex + 1
print(liste)
