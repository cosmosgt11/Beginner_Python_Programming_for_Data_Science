# soru 1

a = "hello world"
type(a)
b = [1, 2, 3, 4]
l = 2 < 3
type(l)
type(b)
c = {"name":"halil",
     "family_name": "ceyran",
     "ages":26}
type(c)
t = ("machine learning", "data science")
type(t)
s = {"miuul", "machine learning", "data science"}
type(s)

# soru 2
text = "the goal is to turn data information, and information to insight."
list(text.upper().split())

# soru 3
lst = ["D", "A", "T", "A", "S", "C", "İ", "E", "N", "C", "E"]
len(lst)
k = lst[0], lst[10]
list(lst[0:4])
lst.pop(8)   # eleman silme
print(lst)
lst.append("T")
print(lst)
lst.pop(10)
lst.insert(8,"N")
print(lst)

# soru 4
dict = {
    "Christin": ["america",18],
    "daisy": ["england",12],
    "antonio": ["spain", 22],
    "dante": ["italy",25]}

print(dict.keys())                       # key değerlerine ulaşır
print(dict.values())                     # value değerlerine ulaşır
dict["daisy"][1] = 13                    # value değerini değiştirir
dict.update({"Ahmet": ["Turkey", 24]})   # yeni bir key ve value ekler
del dict["antonio"]                      # eleman silme
print(dict)

# soru 5
l = [2, 13, 39, 86, 120, 57]
def func(l):
    even_lst = []
    odd_lst = []
    for i in l:
        if i % 2 == 0:
            even_lst.append(i)
        else:
            odd_lst.append(i)
    return even_lst, odd_lst

func(l)

# soru 6
ogrenciler = ["Ali", "Veli", "Ayse", "Talat", "Zeynep", "Ece"]
for index, stdnt in enumerate(ogrenciler):
    if index < 3:
        index += 1
        print("Mühendislik Fakültesi {0}. öğrenci: {1}".format(index,stdnt))
    else:
        index -= 2
        print("Tıp Fakültesi {0}. öğrenci: {1}".format(index,stdnt))


# soru 7
ders_kodu = ["CMP1005","PSY1001","HUK1005","SEN2204"]
kredi = [3,4,2,4]
kontenjan = [30,75,150,25]
for ders_kodu, kredi, kontenjan in zip(ders_kodu, kredi, kontenjan):
    print("Kredisi {0} olan {1} kodlu dersin kontenjanı {2} kişidir.".format(kredi, ders_kodu, kontenjan))


# soru 8
kume1 = set(["data", "python"])
kume2 = set(["data", "function", "qcut", "lambda", "python", "miuul"])

def kume(set1, set2):
    if set1.issuperset(set2):
        print(set1.intersection(set2))
    else:
        print(set2.difference(set1))

kume(kume1, kume2)