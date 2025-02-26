# break & continue & while



salaries = [1000, 2000, 3000, 4000, 5000]

for salary in salaries:
    if salary == 3000:
        break               # break: aranan koşul yakalandığında döngüyü durdur
    print(salary)



for salary in salaries:
    if salary == 3000:
        continue            # continue: aranan koşulu yoksay ve devam et
    print(salary)



# while: -dığı sürece analamına gelir

number = 1
while number < 5:   # Sayı 5'ten küçük olduğu sürece .... yap
    print(number)
    number += 1     # çalışmak için her zaman sayaca ihtiyaç duyar