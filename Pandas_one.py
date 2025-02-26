#############################################
# PANDAS
#############################################

# Pandas Series
# Veri Okuma (Reading Data)
# Veriye Hızlı Bakış (Quick Look at Data)
# Pandas'ta Seçim İşlemleri (Selection in Pandas)
# Toplulaştırma ve Gruplama (Aggregation & Grouping)
# Apply ve Lambda
# Birleştirme (Join) İşlemleri

#############################################
# Pandas Series
#############################################
import pandas as pd

s = pd.Series([10, 77, 12, 4, 5])  # Pandas serieste index bilgisi bir iç özelliktir
type(s)                            # Pandas serileri tek boyutludur
s.index
s.dtype
s.size   # eleman sayısı
s.ndim   # boyut bilgisini verir
s.values
type(s.values)
s.head(3)        # ilk üç ifadeyi getirir
s.tail(3)        # sondan üç ifadeyi getirir



#############################################
# Veri Okuma  (Reading Data)
#############################################
import pandas as pd

df = pd.read_csv("datasets/advertising.csv")  # dosya okumak için kullanılan metod
df.head()                                       # pd.read_okumak_istenen_dosya_türü

# NOT: pandas cheatsheet araması ile pandasda kullanılan bütün metod ve fonksiyonları bulabilirsin



#############################################
# Veriye Hızlı Bakış (Quick Look at Data)
#############################################

import seaborn as sns

df = sns.load_dataset("titanic")  # bu metod seaborn içerisinde önceden konulmuş datasetleri üzerinde çalışma imkanı verir.
df.head()
df.tail(2)     # sondan değerleri getirir
df.shape       # bir dataframe'nin boyut bilgisini görmek için kullanılır
df.info()      # değişkenler, değişken tipleri vb. detaylı bilgi almak için kullanılır
df.columns     # dataframe'nin değişkenlerinin isimlerini verir
df.index       # dataframe'nin index bilgisini verir
df.describe()   # dataframe'nin hızlı bir şekilde özet istatistiklerine erişmek için kullanılır
df.describe().T   # Transpozunu alarak daha okunabilir hale getirir

df.isnull().values.any()   # detaylarına girmeden dataframe'de en az bir tane bile eksiklik var mı? sorusunu sorar
df.isnull().sum()          # detaylarına girmeden kategorik değişkenlerde kaç tane eksik değer vardır? sorusunu sorar
                           # true'ler 1; False'lar 0 olarak hesaplanır

df["sex"].head()             # Dtaframe içerisinden istenen kategorik değşkenin ismi girilerek çağrılabilir
df["sex"].value_counts()     # Bir kategorik değişkende kaç tane sınıf olduğu ve bu sınıfların toplam değerini verir
