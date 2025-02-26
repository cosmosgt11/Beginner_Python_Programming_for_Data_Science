#############################################
# - 5 Korelasyon Analizi (Analysis of Correlation)
#############################################
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = pd.read_csv("datasets/breast_cancer.csv")
df = df.iloc[:, 1:-1]
df.head()

# Hızlı bir şekilde ısı haritası nasıl oluşturulur?,
# Birbiriyle yüksek korelasyona sahip değişkenlerden birisini silmek istersek nasıl yaparız?

# Önce ısı haritası aracılığıyla korelasyonlarına bakılır
# daha sonra yüksek korelasyonlu bazı değişkenler dışarıda bırakılabilir.

num_cols = [col for col in df.columns if df[col].dtype in [int, float]]  # numeric değerli değişkenleri seçtik

corr = df[num_cols].corr()  # korelasyon hesaplamak için 'corr' fonksiyonu kullanılır

# ısı haritası oluşturma
sns.set(rc={'figure.figsize': (12, 12)})
sns.heatmap(corr, cmap="RdBu")
plt.show()

#######################
# Yüksek Korelasyonlu Değişkenlerin Silinmesi
#######################

cor_matrix = df[num_cols].corr().abs()   # ".abs()" mutlak değerini alır bu şekilde -1 ve +1 korelasyonları +1 de sabitlenir

# Dikkat edersek (1,0) ve (0,1) noktasındaki elamanlar aynı ve köşegenler 1; bunları matristen çıkarmamız lazım
#           0         1         2         3
# 0  1.000000  0.117570  0.871754  0.817941
# 1  0.117570  1.000000  0.428440  0.366126
# 2  0.871754  0.428440  1.000000  0.962865
# 3  0.817941  0.366126  0.962865  1.000000

# Çıkardığımız zaman böyle bir matris oluşacak:
# Dikkat edersek köşegenlerin üzerinde kalan sabit kalır; altındaki elemanlar NaN olur, buna göre işlem yaparız
#     0        1         2         3
# 0 NaN  0.11757  0.871754  0.817941
# 1 NaN      NaN  0.428440  0.366126
# 2 NaN      NaN       NaN  0.962865
# 3 NaN      NaN       NaN       NaN

# bÖyle bir işlem yapalım ki kendi verisetimizi 2.matris gibi düzenleyelim
# Numpy içerisinde yer alan bir fonksiyondan yararlanacağız

# Öncelikle 1'lerden oluşan, oluşturduğumuz matris boyutunda bir numpy arrayi oluşturuyoruz --> (np.ones(cor_matrix.shape), k=1)
# sonra bunu asytpe ile True-False ile doldurduk
# daha sonra köşegen elamanlarından kurtulduktan sonra kalanlar True olacağı için
# ".where" ile şu koşulu sağlayanları ata diyerek yeni matrisi oluşturduk
upper_triangle_matrix = cor_matrix.where(np.triu(np.ones(cor_matrix.shape), k=1).astype(bool))

# Eğer aşırı yüksek korelasyon gösteren değerleri silmek istiyorsak:
drop_list = [col for col in upper_triangle_matrix.columns
             if any(upper_triangle_matrix[col]>0.90)]  # %90 korelasyondan büyük olanları siler
cor_matrix[drop_list]         # matris içinde yüksek korelasyonlu olanları seçer
df.drop(drop_list, axis=1)    # .drop metodu ile dataframe içerisinden silinir


# Bu işlemleri problemleştirelim, fonksiyonlaştıralım
# corr_th --> korelasyon eşik değeri
def high_correlated_cols(dataframe, plot=False, corr_th=0.90):
    corr = dataframe.corr()
    cor_matrix = corr.abs()
    upper_triangle_matrix = cor_matrix.where(np.triu(np.ones(cor_matrix.shape), k=1).astype(bool))
    drop_list = [col for col in upper_triangle_matrix.columns if any(upper_triangle_matrix[col] > corr_th)]
    if plot:
        import seaborn as sns
        import matplotlib.pyplot as plt
        sns.set(rc={'figure.figsize': (15, 15)})
        sns.heatmap(corr, cmap="RdBu")
        plt.show()
    return drop_list

high_correlated_cols(df)
drop_list = high_correlated_cols(df, plot=True)
df.drop(drop_list, axis=1)
high_correlated_cols(df.drop(drop_list, axis=1), plot=True)

import matplotlib.pyplot as plt

notlar = [68, 74, 82, 90, 78, 85, 92, 88, 76, 61, 79, 73, 89, 81, 72, 95, 70, 83, 77, 75]

plt.hist(notlar, bins=10, edgecolor='r', alpha=0.7)
plt.xlabel('Notlar')
plt.ylabel('Frekans')
plt.title('Sınav Notları Dağılımı')
plt.show()

