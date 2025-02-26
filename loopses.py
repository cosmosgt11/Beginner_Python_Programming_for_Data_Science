# FOR Loop

students = ["John", "Mark", "Venessa", "Mariam"]
for student in students:
    print(student)

for student in students:
    print(student.upper())


salaries = [1000, 2000, 3000, 4000, 5000]
for salary in salaries:
    print(salary)

for salary in salaries:
    print(int(salary*20/100 + salary))


def new_salary(salary, rate):
    return int(salary*rate/100 + salary)

for salary in salaries:
    print(new_salary(salary, 10))


# Maaşı 3000 yada 3000'den büyük olanlara farklı
# 3000'den az olanlara farklı miktarlarda zam yapan
for salary in salaries:
    if salary >= 3000:
        print(new_salary(salary, 10))
    else:
        print(new_salary(salary, 20))



list2 = list(range(11))
b = 0
for i in list2:
   b += i
   print(b)