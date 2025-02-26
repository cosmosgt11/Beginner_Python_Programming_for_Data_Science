# Uygulama - Mülakat Sorusu


# SORU: Çift sayıların karesi alınarak bir sözlüğe eklenmek istemektedir.
# Key'ler orijinal değerler, Value'ler ise kareleri olacak.


# Klasik method
numbers = range(10)
new_dict = {}
for n in numbers:
    if n % 2 == 0:
        new_dict[n] = n ** 2


# Dict Comprehension
{n: n ** 2 for n in numbers if n % 2 == 0}


