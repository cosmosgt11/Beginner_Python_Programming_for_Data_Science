print("a")
print("a","b")

print("a","b", sep="__")
help(print)    # Fonksiyonun dökümantasyonun gösterir


# YENİ BİR FONKSİYON TANIMLAMA
def calculate(x):
    print(x*2)

calculate(5)

# İKİ ARGÜMANLI/PARAMETRELİ BİR FONKSİYON TANIMLAMA
def summer(arg1, arg2):
    print(arg1 + arg2)

summer(7, 8)

# DOCSTRİNG ---> Fonksiyona herkesin anlayabileceği bilgi notu eklemek.

def summer(arg1, arg2):   # Üç tırnak aç, enter'a bas aşağı in
    """
    Sum of two numbers

    :param arg1: int, float
    :param arg2: int, float
    :return: int, float
    """
    # İstersen farklı bilgi bölümleri ekleyebilirsin
    print(arg1 + arg2)
help(summer)
summer(1, 3)


# FONKSİYONLARIN GÖVDE BÖLÜMÜ

# def function_name(parameter/arguments):
#       statements (function body)

def say_hi(string):
    print(string)
    print("Hi")
    print("Hello")

say_hi("halil")

def calt(arg3, arg4):
    c = arg3+ arg4
    print(c)

calt(12,6)


# Girilen değerleri bir liste içinde saklayacak fonksiyon.

list_store = []
def crelist(x):
    list_store.append(x)
    print(list_store)

crelist('a')


# ÖN tanımlı argümanlar / Parametreler

def divide(a, b):
    print(a / b)

divide(1,2)

def divide(a, b=1):  # b ön tanımlı argümanı b'nin değeri girilmese de fonk.nun çalışmasını sağlar
    print(a / b)

divide(5)

# Birbirini tekrar eden durumlarda fonksiyon yazılır

# RETURN: Fonksiyon Çıktılarını Girdi Olarak Kullanmak

def calculate(varm, moisture, charge):
    varm = varm * 2
    moisture = moisture * 2
    charge = charge * 2
    output = (varm + moisture) / charge
    return varm, moisture, charge, output

print(calculate(98, 12, 78))
type(calculate(98, 12, 78))


# Fonksiyon İçerisinden Fonksiyon Çağırmak

def calc(varm, moisture, charge):
    return int((varm + moisture) / charge)

calc(90, 12, 12) * 10


# Local & Global değişkenler - (Local & Global Variables)

list_store = [1, 2]

def add_element(a, b):         # fonk. içindeki "c" local değişkendir. "list_store" global değişkendir
    c = a * b                  # c fonk. dışına çıkamaz ve fonk. dışında anlam taşımaz
    list_store.append(c)
    print(list_store)

add_element(3, 7)