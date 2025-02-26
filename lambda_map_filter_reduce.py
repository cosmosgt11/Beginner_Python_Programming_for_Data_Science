
# lambda, map, filter, reduce
# Pythonun fonksiyonel programlama yönüne hitap eden,
# vektör seviyesinde işlemler yapma yönünde kullanılan araçlardır.


# lambda: bir tanımlama, atama işlemi yapılmaksızın kullanılabilirdir. Bir fonksiyon tanımlama şeklidir.
# Bir tür kullan at fonksiyonu tanımlar.
new_sum = lambda a, b: a + b
new_sum(2,5)


# MAP: İteratif bir nesne üzerinde(örnek-> liste), döngü kullanılmaksızın işlem yapılmasını sağlar.
salaries = [1000, 2000, 3000, 4000, 5000]

# NORMALDE
def new_salary(salary):
    return int(salary*20/100 + salary)

for salary in salaries:
    print(new_salary(salary))
                                   # yani new_salary fonk.unu for döngüsü gerektirmeden kullanır.
# MAP İLE
list(map(new_salary, salaries))


# Lambda - Map ilişkisi
list(map(lambda x: x * 20 / 100 + x, salaries))




# FILTER: filtreleme işlemleri için kullanılır, kullanım sıklığı çok düşüktür
list_store = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list(filter(lambda x: x % 2 == 0, list_store))



# REDUCE: İndirgemek demektir.  # öncelikli olarak import etmemiz gerekiyor kullanamak için
from functools import reduce
list_store1 = [1, 2, 3, 4]
reduce(lambda a, b: a + b, list_store1)
