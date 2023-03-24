import random as r
a = input("Введите Камень, Ножницы или Бумагу:  ")
b = r.randint(1, 3)
if b == 1:
    b = "Бумага"
elif b == 2:
    b = "Ножницы"
elif b == 3:
    b = "Камень"
else:
    print("Ошибка")
print(a + " - твой знак")
print(b + " - мой знак")