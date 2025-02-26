#############################################
# PANDAS
#############################################

# Pandas'ta Seçim İşlemleri (Selection in Pandas)
# Toplulaştırma ve Gruplama (Aggregation & Grouping)
# Apply ve Lambda
# Birleştirme (Join) İşlemleri


#############################################
# Pandas'ta Seçim İşlemleri (Selection in Pandas)
#############################################
import pandas as pd
import seaborn as sns
df = sns.load_dataset("titanic")
df.head()

# Dış Özellikler
df.index
df[0:13]    # Slice (belirli bir araliğı kesme, alt küme oluşturma): 0 dahil 13 hariç

df.drop(0, axis=0).head()   # Silme işlemi  - axis = satır
# sıfırıncı indexteki sıfırıncı satırı sil

delete_indexes = [1, 3, 5, 7]          # silme işlemi liste gönderilerek de yapılabilir
df.drop(delete_indexes, axis=0).head(10)

# Bu değişikliği kalıcı olarak yapabilmek için iki yöntem kullanılır:
# df = df.drop(delete_indexes, axis=0)     yeniden kendisine atayabilirsin
# df.drop(delete_indexes, axis=0, inplace=True)  inplace argümanı kullanılabilir
# inplace argümanı bir çok yöntemde değişikliğin kalıcılığını sağlamak için kullanılır


#############################################
# Değişkeni Indexe Çevirmek
#############################################
df["age"].head()        # df.["kategorik değişken"] veya df.age --> değişken seçme
df.age.head()

df.index = df.age         # index sütununa yaş değişkenini atadı
df.drop("age", axis=1).head()   # yaş değişkeni sütununu sildi

# NOT: Python'da Sütunları silmek için, axis argümanını 1 olarak ayarlayarak drop fonksiyonunu kullanabilirsiniz
# NOT: Satır silmek için, axis argümanını 0 olarak kullanmamız gerekir

df.drop("age", axis=1, inplace=True)
df.head()

#############################################
# Indexi Değişkene Çevirmek
#############################################
# birinci yol
df.index
df["age"] = df.index
df.head()

df.drop("age", axis=1, inplace=True)

# İkinci yol
df.reset_index().head()  # İndexte yer alan değeri siler ve bunu yeni bir değişken olarak ekler
df = df.reset_index()


#############################################
# Değişkenler Üzerinde İşlemler
#############################################
pd.set_option('display.max_columns', None)   # gelen df ortasındaki '...' lar gözükmesin diye set edilir
df = sns.load_dataset("titanic")
df.head()

"age" in df                  # bir dataframe'de herhangi değişkenin varlığını sorgulama

df["age"].head()             # Bu şekilde bir seçim bir pandas serisi verir
type(df["age"].head())

df[["age"]].head()           # seçimin sonucunun dataframe olarak kalmasını istiyorsan iki kare parantezli seçilir
type(df[["age"]].head())

df[["age", "alive"]]         # birden fazla değişken seçmek için kullanılır

col_names = ["age", "adult_male", "alive"]  # başka bir liste ile değişken seçmek
df[col_names]
type(df[col_names])

df["ages2"] = df["age"]**2         # dateframe yeni bir değişken ekleme
df["ages3"] = df["age"] / df["ages2"]

df.drop("ages3", axis=1).head()   # bir değişkeni silmek
df.drop(col_names, axis=1).head()       # listede yazılı olan değişkenleri silmek

# İçerisinde belirli bir ifadeyi taşıyan değişkenleri bulmak ve silmek
# contains: bir string metodudur. Kendisine verilen iafdeyi string içerisinde arar

df.loc[:, df.columns.str.contains("age")].head()  # belirtilen seçme için loc metodu kullanılır

df.loc[:, ~df.columns.str.contains("age")].head() # tilda(~) işareti değildir anlamına gelir
                                                  # yani "age" içermeyen tüm değişkenleri seç


#############################################
# loc & iloc Yapıları
#############################################
# iloc, Pandas DataFrame ve Series üzerinde konum tabanlı dilimleme ve indeksleme işlemlerini
# gerçekleştirmek için kullanılır.
# iloc ile belirli satır ve sütunları, tamsayı indeksleri kullanarak seçebilirsiniz

# loc, Pandas DataFrame ve Series üzerinde etiket bazlı dilimleme ve indeksleme
# işlemlerini gerçekleştirmek için kullanılır.
# loc ile belirli satır ve sütunları, etiketleri kullanarak seçebilirsiniz.

pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")
df.head()

# iloc: integer based selection
df.iloc[0:3]             # sıfırdan üçe kadar satırları seçer - 3 dahil değil
df.iloc[0, 0]            # virgülden önce satır, sonrası sütun -- 0. satır 0. sütundaki elamanı getir
df.iloc[0:3, 0:3]        # ilk 3 satır ve ilk 3 sütunu getir

# loc: label based selection
df.loc[0:3]              # indexi üçe kadar olan değişkenleri seçer  - 3 dahil
df.loc[0:3, "age"]       # age etiketini taşıyan değişkenlerin indexi 3'e kadar olan satırlarını getir

col_me = ["age", "embarked", "alive"]
df.loc[0:3, col_me]      # listedeki elamanları etiket olarak arayıp getirir


#############################################
# Koşullu Seçim (Conditional Selection)
#############################################
pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")
df.head()

df[df["age"] > 50].head()     # Dataframede yaşı 50'den büyük olanları seçer (değişken koşulu)

df[df["age"] > 50]["age"].count()    # Dataframede yaşı 50'den büyük olan kaç kişi var?

df.loc[df["age"] > 50, "class"].head()  # Dataframede yaşı 50'den büyük olanların class bilgileri?

df.loc[df["age"] > 50, ["age", "class"]].head()   # Dataframede yaşı 50'den büyük olanların hem class hem yaş bilgileri?

# Not: birden fazla koşul giriliyorsa koşulların parantez içine alınması gerekir
df.loc[(df["age"] > 50) & (df["sex"] == "male"), ["age", "class"]].head()
# Dataframede yaşı 50'den büyük olan ve cinsiyeti erkek olanlar (İki koşul birlikte)

df_new = df.loc[(df["age"] > 50) & (df["sex"] == "male")
       & ((df["embark_town"] == "Cherbourg") | (df["embark_town"] == "Southampton")),
       ["age", "class", "embark_town"]]  # df içinde 50'den büyük, erkek, "Cherbourg" YADA "Southampton" da binen

df_new["embark_town"].value_counts()