# 4.	Умната Лили
# Лили вече е на N години. За всеки свой рожден ден тя получава подарък.
# •	За нечетните рождени дни (1, 3, 5...n) получава играчки.
# •	За четните рождени дни (2, 4, 6...n) получава пари.
# За втория рожден ден получава 10.00 лв, като сумата се увеличава с 10.00 лв.,
# за всеки следващ четен рожден ден (2 -> 10, 4 -> 20, 6 -> 30...и т.н.).
# През годините Лили тайно е спестявала парите.
# Братът на Лили, в годините, които тя получава пари, взима по 1.00 лев от тях.
# Лили продала играчките получени през годините, всяка за P лева и добавила сумата към спестените пари.
# С парите искала да си купи пералня за X лева.
# Напишете програма, която да пресмята, колко пари е събрала и дали ѝ стигат да си купи пералня.
age = int(input())
washing_machine_price = float(input())
toy_price = int(input())
totall_money = 0
birthday_money = 0
toy = 0
for even_odd in range(1, age + 1):
    if even_odd % 2 != 0:
        toy += 1
    else:
        birthday_money += 10
        totall_money += birthday_money - 1
totall_money += toy * toy_price

# •	Ако парите на Лили са достатъчни:
# o	"Yes! {N}" - където N е остатъка пари след покупката
diff = abs(totall_money - washing_machine_price)
if washing_machine_price <= totall_money:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")
# •	Ако парите не са достатъчни:
# o	"No! {М}" - където M е сумата, която не достига
# Числата N и M трябва да за форматирани до вторият знак след десетичната запетая.
