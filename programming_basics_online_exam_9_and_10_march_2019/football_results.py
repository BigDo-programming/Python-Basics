# Футболен отбор участва в благотворителен турнир. На този турнир отборът играе три мача като домакин.
# Да се напише програма, която изчислява колко победи, равенства и загуби има отборът по време на турнира,
# спрямо резултатите от мачовете.
# *Забележка: Отборът винаги е домакин, следователно първата цифра от резултата съответства на головете вкарани от него.
# Вход
# От конзолата се четат 3 реда:
# 1.	Резултат от първия мач – текст
# 2.	Резултат от втория мач – текст
# 3.	Резултат от третия мач – текст

# Резултатите ще са в следния формат: "2:0", "0:1", "1:1" и т.н.
# /броят голове винаги ще бъде едноцифрено число/

result_of_the_first_match = input()
result_of_the_second_match = input()
result_of_the_third_match = input()
win = 0
lose = 0
equal = 0

if result_of_the_first_match[0] > result_of_the_first_match[2]:
    win += 1
elif result_of_the_first_match[0] < result_of_the_first_match[2]:
    lose += 1
elif result_of_the_first_match[0] == result_of_the_first_match[2]:
    equal += 1
if result_of_the_second_match[0] > result_of_the_second_match[2]:
    win += 1
elif result_of_the_second_match[0] < result_of_the_second_match[2]:
    lose += 1
elif result_of_the_second_match[0] == result_of_the_second_match[2]:
    equal += 1
if result_of_the_third_match[0] > result_of_the_third_match[2]:
    win += 1
elif result_of_the_third_match[0] < result_of_the_third_match[2]:
    lose += 1
elif result_of_the_third_match[0] == result_of_the_third_match[2]:
    equal += 1


print(f"Team won {win} games.")
print(f"Team lost {lose} games.")
print(f" Drawn games: {equal}")
