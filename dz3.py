spisok = [1.78, 1.89, 1.55, 1.88, 1.68]
petya = float(input())
spisok.append(petya)
spisok.sort()
spisok.reverse()
print(spisok)
print(spisok.index(petya) + 1)


