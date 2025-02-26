#############################################
# Veri Görselleştirme: Matplotlib & Seaborn
#############################################

#############################################
# MATPLOTLİB
#############################################
# Low decerelidir.
# Kategorik değişken: sütun grafik, countplot bar
# Sayısal değişken: histogram, boxplot


#############################################
# Kategorik Değişken Görselleştirme
#############################################
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.width',500)
df = sns.load_dataset("titanic")
df.head()

df["sex"].value_counts().plot(kind='bar')        # value_count --> kategorik değişken görselleştirmede kullanılır
                                                 # kind='grafik türü bilgisi' bar= sütun grafiği
plt.show()                                       # grafiği ekrana yazdırma komutu


#############################################
# Sayısal Değişken Görselleştirme
#############################################

# - Histogram çizdirme     - histogram = aralık grafiği
plt.hist(df["age"])
plt.show()

# - Boxplot
plt.boxplot(df["fare"])
plt.show()


#############################################
# Matplotlib'in Özellikleri
#############################################
# Yapısı itibarıyla katmanlı bir şekilde veri görselleştirme imkanı sağlar.
# Yani bir katmanda bir görsel, diğer katmanda isimlendirme gibi farklı katmanlarda manipülasyon izni verir

# - plot
x = np.array([1, 0])
y = np.array([0, 150])

plt.plot(x, y)  # iki arrayi görselleştirmek için kullanılır
plt.show()

plt.plot(x, y, 'o')  # grafiğin nokatalarını işaretler
plt.show()

x = np.array([2, 4, 6, 8, 10])
y = np.array([1, 3, 5, 7, 9])
plt.plot(x, y)
plt.show()

plt.plot(x, y, 'o')  # grafiğin nokatalarını işaretler
plt.show()


# - Marker
y = np.array([13, 28, 11, 100])

plt.plot(y, marker='o')  # y noktalarına marker koy
plt.show()

plt.plot(y, marker='*')  # y noktalarına marker koy
plt.show()
# Daha bir çok marker bulunur


# - Line
y = np.array([13, 28, 11, 100])
plt.plot(y, linestyle="dashed")    # kesikli line
plt.show()

plt.plot(y, linestyle="dotted")    # noktalı line
plt.show()

plt.plot(y, linestyle="dashdot", color="r")    # kesikli-noktalı ve kırmızı renkli line
plt.show()


# - Multiple Lines
x = np.array([23, 18, 31, 10])
y = np.array([13, 28, 11, 100])
plt.plot(x)
plt.plot(y)
plt.show()


# - Labels (etiketler)
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.plot(x, y)

plt.title("Bu ana başlık")   # ana başlık ekleme
plt.ylabel("y ekseni")       # y ekseni isimlendirma
plt.xlabel("x ekseni")       # x ekseni isimlendirme

plt.grid()      # grafiğe ızgara eklemek
plt.show()


# - Subplot --> Birden fazla görseli birlikte gösterilmesi

# plot 1
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.subplot(1, 2, 1)
plt.title("1")
plt.plot(x, y)

# plot 2
a = np.array([8, 8, 9, 10, 11, 15, 12, 15, 11])
b = np.array([24, 23, 21, 19, 24, 20, 20, 22, 21])
plt.subplot(1, 2, 2)
plt.title("2")
plt.plot(a, b)
plt.show()


#############################################
# SEABORN
#############################################
# high level

df = sns.load_dataset("tips")
df.head()

# - kategorik Değişken Görselleştirme
df["sex"].value_counts()
sns.countplot(x=df["sex"], data=df)      # ikinci argünam veri setini göster demektir
plt.show()

# - Sayısal Değişken Görselleştirme
sns.boxplot(x=df["total_bill"])
plt.show()

df["total_bill"].hist()
plt.show()