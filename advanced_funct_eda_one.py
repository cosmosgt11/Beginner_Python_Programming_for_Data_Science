#############################################
# - GELİŞMİŞ FONKSİYONEL KEŞİFÇİ VERİ ANALİZİ (ADVANCED FUNCTIONAL EDA)
#############################################
# - 1 Genel resim
# - 2 Kategorik Değişken Analizi (Analysis of Categorical Variables)
# - 3 Sayısal Değişken Analizi (Analysis of Numerical Variables)
# - 4 Hedef Değişken Analizi (Analysis of Target Variables)
# - 5 Korelasyon Analizi (Analysis of Correlation)


#############################################
# - 1 Genel resim
#############################################

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
df.head()
df.tail()        # sondan değerleri getirir
df.shape         # bir dataframe'nin boyut bilgisini görmek için kullanılır
df.info()        # değişkenler, değişken tipleri vb. detaylı bilgi almak için kullanılır
df.columns       # dataframe'nin değişkenlerinin isimlerini verir
df.index         # dataframe'nin index bilgisini verir
df.describe()    # dataframe'nin hızlı bir şekilde özet istatistiklerine erişmek için kullanılır
df.describe().T  # Transpozunu alarak daha okunabilir hale getirir

df.isnull().values.any()  # detaylarına girmeden dataframe'de en az bir tane bile eksiklik var mı? sorusunu sorar
df.isnull().sum()         # detaylarına girmeden kategorik değişkenlerde kaç tane eksik değer vardır? sorusunu sorar


# Bazı metodları veri seti üzerinde kullanabileceğin özel fonksiyona dönüştürme
def check_df(dataframe, head=5):      #dataframe: neyi analiz edecegiz, head: satır gösterilmesi gerekirse kaç tane?
    print("#################### Shape ###############")
    print(dataframe.shape)
    print("#################### Types ###############")
    print(dataframe.dtypes)
    print("#################### Head ###############")
    print(dataframe.head(head))
    print("#################### Tail ###############")
    print(dataframe.tail(head))
    print("#################### NA ###############")
    print(dataframe.isnull().sum())
    print("#################### Quantities ###############")
    print(dataframe.describe([0, 0.05, 0.50, 0.95, 0.99, 1]).T)

check_df(df)


#############################################
# - 2 Kategorik Değişken Analizi (Analysis of Categorical Variables)
#############################################
# Genellenebilir, problematik olarak özel tanımlanmış farklı değişken tiplerini yakalayan
# ve bunlar üzerinde analiz yapmamızı sağlayan fonksiyonlar

df["embarked"].value_counts()  # tek bir değişkeni analiz etme
df["sex"].unique()             # hangi farklı değerlerin olduğunu ve tipini gösterir (eşsiz sınıf)
df["sex"].nunique()            # farklı değerlerin sayısı .n(umber)unique (eşsiz sınıf sayısı)


# Değişken tipi categoric olarak gözüken (1. adım) ve
# değişken tipi categoric olarak gözükmese de aslında categoric olan (2. adım) ve
# Category olarak gözüken ama olmayan (3. adım) değişkenleri yakalama
# Yakalanan değişkenleri birleştirme (4. adım)

# ----- ADIM 1 -----
# tüm kolonlarda gez, yakaladığın veri yapılarının tip bilgisini kontrol et
# eğer tip bilgisi object, category veya bool barındırıyorsa bunları seç
# str(df[col].dytpes)  --> her kolonun tipini stringe çevir
cat_cols = [col for col in df.columns if str(df[col].dtypes) in ["category", "object", "bool"]]

# ----- ADIM 2 -----
# tipi integer yada float olup eşsiz sınıf sayısı belirli bir değerden küçük ve tipi int veya float olanları yakala
num_but_cat = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes in ["int64", "float64"]]

# ----- ADIM 3 -----
# Kardinalitesi yüksek değişkenleri (açıklanabilirlik taşımayacak kadar fazla sınıfı olan) bulma
# örnek olarak isim-soyisim değişkenleri verilebilir
cat_but_car = [col for col in df.columns if df[col].nunique() > 10 and str(df[col].dtypes) in ["category", "object"]]

# ----- ADIM 4 -----
cat_cols = cat_cols + num_but_cat
cat_cols = [col for col in cat_cols if col not in cat_but_car]

df[cat_cols].nunique()

[col for col in df.columns if col not in cat_cols]  # sadece gerçek kategorik olmayan değişkenler


#############################################
# - 2 Kategorik Değişken Analizi II (Analysis of Categorical Variables II)
#############################################
# Yaptığımız yakalamayı fonksiyonel olarak değerlendirmek-kullanmak

df["survived"].value_counts()
100 * df["survived"].value_counts() / len(df)  # sınıfların yüzdelik bilgisi

def cat_summery(dataframe, col_name):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("###################################")

cat_summery(df, "sex")

for col in cat_cols:
    cat_summery(df, col)

# cat_summery fonk.na grafik özelliği de ekleyeceğiz
def cat_summery(dataframe, col_name, plot=False):                    # ekstra olarak sütun grafiğini oluştursun, kategoric değişken olduğu için
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * df[col_name].value_counts() / len(dataframe)}))
    print("###################################")

    if plot:
        sns.countplot(x=dataframe[col_name], data=dataframe)
        plt.show(block=True)

cat_summery(df, "sex", plot=True)

for col in cat_cols:
    if df[col].dtypes == "bool":
        print("adhfguodfhguahg")
    else:
        cat_summery(df, col, plot=True)


df["adult_male"].astype(int)     # bool tipi olan değişkeni integere çevirdi True -> 1: False ->0 oldu

for col in cat_cols:
    if df[col].dtypes == "bool":
        df[col] = df[col].astype(int)
        cat_summery(df, col, plot=True)
    else:
        cat_summery(df, col, plot=True)