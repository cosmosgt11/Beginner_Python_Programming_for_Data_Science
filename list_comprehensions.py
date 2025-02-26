
# Comprehensions  --> Birden fazla satır ve kod ile yapılabilecek işlemleri
# istediğimiz çıktı veri yapısına göre tek bir satırda yapmamızı sağlayan yapılardır.

# LİST Comprehension  --> çıktısı listedir.

salaries = [1000, 2000, 3000, 4000, 5000]

def new_salary(x):
    return x * 20 / 100 + x

for salary in salaries:
    print(new_salary(salary))


nul_list = []
for salary in salaries:
    nul_list.append(new_salary(salary))
    print(nul_list)

nul_list = []
for salary in salaries:
    if salary > 3000:
        nul_list.append(new_salary(salary))
    else:
        nul_list.append(new_salary(salary * 2))


# Yukarıda 21 ve 26. arasında kalan satırları tek bir satırda yapabiliriz
[new_salary(salary) if salary < 3000 else new_salary(salary * 2) for salary in salaries]

# Bu yapı list comprehension yapısıdır ve çok önemlidir.
# List comprehension içerisinde döngü, if-else yapısı ve fonksiyonlar kullanılabilir

# Adım adım list comprehension yapısı.
# [] --> Öncelikle list oluşturma yapısıyla başlar. Bu çıktının liste olmasını sağlar

[salary * 2 for salary in salaries]  # for ile salaries içinde gez, her bir elemanı 2 ile çarp

[salary * 2 for salary in salaries if salary < 3000]  # for ile salaries içinde gez, ve 3000'den küçük olan elemanları 2 ile çarp: değilse bişey yapma

# NOT: Comprehensions içerisinde sadece if kullanıyorsanız sağ tarafa; else yapısıda varsa for bloğu sağda kalır.

[salary * 2  if salary < 3000 else salary * 0 for salary in salaries] # for ile salaries içinde gez, ve 3000'den küçük olan elemanları 2 ile çarp: değilse sıfır ile çarp


# NOT: İstediğimiz bir fonksiyonu en solda kullanmamız gerekir

[new_salary(salary * 2) if salary < 3000 else new_salary(salary * 0.2) for salary in salaries]


# İstenilen öğrenci isimlerini büyük; istenmeyenleri küçük yazacak comprehension yapısı
students = ["John", "Mark", "Venessa", "Mariam"]  # öğrenci listesi
students_no = ["John", "Venessa"]                 # istenmeyen öğrenciler listesi

[student.lower() if student in students_no else student.upper() for student in students]