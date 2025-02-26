#######  NUMPY  #######
# - Bilimsel hesaplamalar için kullanılır
# - Çok-boyutlu arrayler ve Matrisler üzerinde işlem yapmaya imkan verir
# - Listelerden farklı olarak: verimli veri saklama ve vektörel operasyonlar yapabilir
# - İçerisindeki veriyi Fix type (sabitlenmiş tip) olarak tutar, bu listelere kıyasla hızlı işlem yeteneği sağlar


# NumPy Kütüphanesini İmport Etme

import numpy as np

# - Klasik Yöntem -
a = [1, 2, 3, 4]
b = [2, 3, 4, 5]
ab = []
for i in range(0, len(a)):
    ab.append(a[i] * b[i])

# - NumPy ile aynı işlem -
a = np.array([1, 2, 3, 4])
b = np.array([2, 3, 4, 5])
a * b



######  NumPy Array'i Oluşturma (Creating NumPy Arrays)  ######
# - Bir tür veri yapısıdır; int, float gibi.
# - Pratikte sıfırdan oluşturulmaz, çalışma esnasında bazı veri yapılarından dönüştürülür.

np.array([1, 2, 3, 4, 5])   # --> Liste üzerinden np array oluşturma
type(np.array([1, 2, 3, 4, 5]))

# - Sıfırdan Array Oluşturma -
np.zeros(10, dtype= int)   # Girdiğin sayı adedince sıfır oluşturan metod
                                 # dtype ile elemanların tipi belirlenir

np.random.randint(0, 10, size= 10)  # 0 ila 10 arasında rasgele 10 tane eleman ile oluşturulan array

np.random.normal(10, 4, (3, 4))  # Birinci argüman: ortalaması
                                                # İkinci argüman: standart sapması
                                                # Üçüncü argüman: boyutu - olan bir array oluştur



######  NumPy Array Özellikleri  ######
# ndim: boyut sayısı
# shape: boyut bilgisi
# size: toplam eleman sayısı
# dtype: array veri tipi

a = np.random.randint(10, size= 5)
a.ndim
a.shape                                # her boyuttaki eleman sayısı gelir
a.size
a.dtype



######  Yeniden Şekillendirme (Reshaping)  ######
# Bir metoddur

np.random.randint(1, 10, size= 9)   # Örneğin bunu 3x3'lük bir matrise dönüştürmek için reshaping kullanılr
np.random.randint(1, 10, size= 9).reshape(3, 3)
# veya
ar = np.random.randint(1, 10, size= 9)
ar.reshape(3, 3)



######  Index Seçimi (Index Selection)  ######
# Önemli bir konudur.

a = np.random.randint(10, size= 10)
a[0]         # Sıfırıncı elemana gider
a[0:5]       # SIıfr ile beş arasına git. Sol taraftaki dahil, sağ taraftaki hariç
a[0] = 999   # ilgili indexteki elemanı değiştirir

# İki boyutlu arraylerde seçim işlemi
m = np.random.randint(10, size=(3, 5))
m[2, 4]      # Virgülden önce satırları, virgülden sonrası sütunları temsil eder
m[0, 0] = 3
m[:, 0:2]



###### Fancy Index ######
# Bir NumPy array'ine bir liste girdiğinizde, listeye karşılık gelen indexleri çağırmayı sağlar

v = np.arange(0, 30, 3)    # Sıfırdan başla 3'er artarak 30'a kadar array oluştur, 30 dahil değil
v[1]
v[4]

catch = [1, 2, 3]
v[catch]



###### NumPy'da Koşullu İşlemler (Conditions on NumPy)  ######

t = np.arange(1, 6, 1)

# t array'indeki 3'ten küçük elemanları seçecek kod dizisi

# Klasik Yöntem
s = []
for i in t:
    if i < 3:
        s.append(i)

# NumPy ile
t[t < 3]             # t içerisinde 3'ten küçük olanları çağır
t[t != 3]            # t içerisinde 3'e eşit olmayanları çağır



######  Matematiksel İşlemler (Mathematical Operations)  ######

t = np.arange(1, 6, 1)
t / 5
t * 5 ** 2

np.subtract(t, 1)     # çıkarma işlemi için
np.add(t, 1)          # toplama işlemi
np.mean(t)            # ortalama işlemi
np.sum(t)             # toplam alma işlemi
np.min(t)
np.max(t)
np.var(t)             # varyans işlemi

# - NumPy'da İki Bilinmeyenli Denklem Çözümü -

# 5*x1 + x2 = 12    birinci denklem
# x1 + 3*x2 = 10    ikinci denklem

a = np.array([[5, 1], [1, 3]])   # [[x1'in katsayıları],[x2'nin katsayıları]]
b = np.array([12, 10])           # [sonuçlar]

np.linalg.solve(a, b)            # metodu kullanılarak çözülür