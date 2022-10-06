
friends = ["Алексей Иванов", "Дмитрий Алексеев", "Роман Кукухин", "Валерий Пономарев"]
print(*friends, sep=',')
friends.remove("Алексей Иванов")
print("Алексей Иванов не сможет прийти.")
friends.insert(0, "Данил Дубровин")
print(*friends, sep=',')
del friends[0]
friends.insert(1,"Данил Дубровин")
print(*friends, sep=',')
del friends [1]
friends.append("Данил Дубровин")
print(*friends, sep=',')
