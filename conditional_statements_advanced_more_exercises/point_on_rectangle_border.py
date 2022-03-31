# 8.	Точка върху страната на правоъгълник
# Напишете програма, която проверява дали точка {x, y} се намира върху някоя от страните на правоъгълник {x1, y1} – {x2, y2}.
# Входните данни се четат от конзолата и се състоят от 6 реда въведени от потребителя:
# десетичните числа x1, y1, x2, y2, x и y (като се гарантира, че x1 < x2 и y1 < y2).

# Да се отпечата "Border" (точката лежи на някоя от страните) или "Inside / Outside" (в противен случай).


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x = float(input())
y = float(input())


if x == x1 and y1 <= y <= y2:
    print("Border")
elif x == x2 and y1 <= y <= y2:
    print("Border")
elif y == y1 and x1 <= x <= x2:
    print("Border")
elif y == y2 and x1 <= x <= x2:
    print("Border")

else:
    print("Inside / Outside")

