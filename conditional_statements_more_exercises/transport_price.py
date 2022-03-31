# Студент трябва да пропътува n километра. Той има избор измежду три вида транспорт:
# •	Такси. Начална такса: 0.70 лв. Дневна тарифа: 0.79 лв. / км. Нощна тарифа: 0.90 лв. / км.
# •	Автобус. Дневна / нощна тарифа: 0.09 лв. / км. Може да се използва за разстояния минимум 20 км.
# •	Влак. Дневна / нощна тарифа: 0.06 лв. / км. Може да се използва за разстояния минимум 100 км.
# Напишете програма, която въвежда броя километри n и период от деня (ден или нощ)
# и изчислява цената на най-евтиния транспорт.
n = int(input())
day_or_night = input()
day_t = 0
night_t = 0
if n < 20:
    if day_or_night == 'day':
        day_t = (0.79 * n) + 0.70
    elif day_or_night == 'night':
        night_t = (0.90 * n) + 0.70
elif n < 100:
    if day_or_night == 'day':
        day_t = 0.09 * n
    elif day_or_night == 'night':
        night_t = 0.09 * n
elif n >= 100:
    if day_or_night == 'day':
        day_t = 0.06 * n
    elif day_or_night == 'night':
        night_t = 0.06 * n
# Да се отпечата на конзолата най-ниската цена за посочения брой километри,
# форматирана до втория знак след десетичния разделител.
if day_or_night == 'day':
    print(f'{day_t:.2f}')
else:
    print(f'{night_t:.2f}')