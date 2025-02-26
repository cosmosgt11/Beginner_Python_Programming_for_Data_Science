
# Enumerate: Otomatik Counter/Indexer ile for loop
# Otomatik indeks üretir.
# For loop ile birlikte kullanılır.

# İteratif yani üzerinde gezilebilir (örneğin bir liste içerisinde gezerken)
# ilgili elemanlara belirli bir işlem uygularken aynı zamanda işlem uygulanan elamanların
# indeks bilgisini de tutabilen ve bu indeks bilgisine göre de bir işlem yapabilmemizi sağlayan bir yapıdır.


students = ["John", "Mark", "Venessa", "Mariam"]

for student in students:
    print(student)

for index, student in enumerate(students, 1):   # indeks 1'den başlasın diye 1 yazdık
    print(index, student)
# Liste içndeki her bir elemanla eşleşmiş(match) indeks üretir
# Önce indeks sonra eleman ismi yazılır



# Students listesindeki öğrencileri indeks numarasına göre farklı listelere ayıran kod bloğu
A = []
B = []
for index, student in enumerate(students):
    if index % 2 == 0:                      # burada indeksler üzerinde işlem yapar
        A.append(student)                   # burada elemanlar üzerinde işlem yapar
    else:
        B.append(student)
    print(A, B)