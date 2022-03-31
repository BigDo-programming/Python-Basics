# 7.	Хотелска стая
# Хотел предлага 2 вида стаи: студио и апартамент. Напишете програма,
# която изчислява цената за целия престой за студио и апартамент. Цените зависят от месеца на престоя:

# Май и октомври	         Юни и септември	           Юли и август
# Студио - 50 лв./нощувка	Студио - 75.20 лв./нощувка	Студио - 76 лв./нощувка
# Апартамент - 65 лв./нощувка	Апартамент - 68.70 лв./нощувка	Апартамент - 77 лв./нощувка

# Предлагат се и следните отстъпки:
# •	За студио, при повече от 7 нощувки през май и октомври : 5% намаление.
# •	За студио, при повече от 14 нощувки през май и октомври : 30% намаление.
# •	За студио, при повече от 14 нощувки през юни и септември: 20% намаление.
# •	За апартамент, при повече от 14 нощувки, без значение от месеца : 10% намаление.

# Вход
# Входът се чете от конзолата и съдържа точно 2 реда, въведени от потребителя:
# •	На първия ред е месецът - May, June, July, August, September или October;
# •	На втория ред е броят на нощувките - цяло число.
# Изход
# Да се отпечатат на конзолата 2 реда:
# •	На първия ред: "Apartment: {цена за целият престой} lv."
# •	На втория ред: "Studio: {цена за целият престой} lv."
# Цената за целия престой да е форматирана с точност до два знака след десетичната запетая.
month = input()
number_of_nights = int(input())
studio = 0
apartment = 0
if month == 'May' or month == 'October':
    studio = 50
    apartment = 65
    if 7 < number_of_nights < 14:
        studio *= 0.95
    elif number_of_nights > 14:
        studio *= 0.7
elif month == 'June' or month == 'September':
    studio = 75.20
    apartment = 68.70
    if number_of_nights > 14:
        studio *= 0.80
elif month == 'July' or month == 'August':
    studio = 76
    apartment = 77
if number_of_nights > 14:
    apartment *= 0.9
total_a = number_of_nights * apartment
total_s = number_of_nights * studio
print(f"Apartment: {total_a:.2f} lv.")
print(f"Studio: {total_s:.2f} lv.")
