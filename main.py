liste = [5, 10, 5, 8, 7, 1, 8, 5]
flag = 0
currentIndex = 0
print(liste)
while currentIndex < (len(liste)-1):
    i = currentIndex + 1
    while i < len(liste):                       
        if liste[currentIndex] == liste[i]: """find the duplicate items""""
            liste.pop(i)                    """pop duplicate item""""
            flag = 1                        """keep flag for deleting current index""""
        else:
            i = i + 1                       """if pass the first if case,increase the i and look at the next item"""
    if flag == 1:
        liste.pop(currentIndex)             """pop the item of the current index with using flag"""
        currentIndex = -1                   """if any item deleted, current index has to be zero. current index is -1 because it will increase next line. """ 
        flag = 0
    currentIndex = currentIndex + 1         """increase the current item for next step"""
print(liste)
