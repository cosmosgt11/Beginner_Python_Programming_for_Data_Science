
# Mülakat_alternating kod bloğunun enumerate ile yazılması
# İlgili soru: verilen stringin çift indeksleri büyük, tek indeksleri küçük yazdıracak kod bloğu.


def analter(string1):
    new_str = " "
    for index, letter in enumerate(string1):
        if index % 2 == 0:
            new_str += letter.upper()
        else:
            new_str += letter.lower()
    print(new_str)

analter("hi my name is john and i am learning python")
