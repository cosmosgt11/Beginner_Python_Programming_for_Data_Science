# Dict comprehension

dict1 = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4}

dict1.keys()
dict1.values()
dict1.items()


# k: keys
# v: values

{k: v ** 2 for (k, v) in dict1.items()}  # dict.items içinde gez, ilki k; ikinciyi v olarak ata -
                                         # k'lar sabit kalsın, v'lerin karesini al

{k.upper(): v for (k, v) in dict1.items()}  # K'ları büyült, v'lere dokunma