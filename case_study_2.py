import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)

import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns
df.info()

# List Comprehension
# Görev 1:  List Comprehension yapısı kullanarak car_crashes verisindeki numeric değişkenlerin isimlerini büyük
#  harfe çeviriniz ve başına NUM ekleyiniz.

["NUM_" + col.upper() if df[col].dtype != "O" else col.upper() for col in df.columns]


# Görev 2:  ListComprehension yapısı kullanarak car_crashes verisinde isminde "no" barındırmayan
#  değişkenlerin isimlerinin sonuna "FLAG" yazınız.

[col.upper() + "_FLAG" if "no_" not in col else col.upper() for col in df.columns]


# Görev 3:  ListComprehension yapısı kullanarak aşağıda verilen değişken isimlerinden FARKLI olan
#  değişkenlerin isimlerini seçiniz ve yeni bir dataframe oluşturunuz.

og_list = ["abbrev", "no_previous"]
new_cols = [col for col in df.columns if col not in og_list]
new_df = df[new_cols]
new_df.head()


# Pandas Alıştırmalar
# Görev 1:  Seaborn kütüphanesi içerisinden Titanic veri setini tanımlayınız.
df = sns.load_dataset("titanic")
df.head()
df.shape

# Görev 2:  Titanic veri setindeki kadın ve erkek yolcuların sayısını bulunuz.
df["sex"].value_counts()

#  Görev 3:  Her bir sutuna ait unique değerlerin sayısını bulunuz.
df.nunique()

# Görev 4: pclass değişkeninin unique değerleri bulunuz.
df["pclass"].nunique()

# Görev 5:  pclass ve parch değişkenlerinin unique değerlerinin sayısını bulunuz.
df[["pclass" , "parch"]].nunique()

# Görev 6:  embarked değişkeninin tipini kontrol ediniz. Tipini category olarak değiştiriniz ve tekrar kontrol ediniz.
df["embarked"].dtype
df["embarked"] = df["embarked"].astype('category')
df["embarked"].dtype
df.info()

# Görev 7: embarked değeri C olanların tüm bilgelerini gösteriniz.
df[df["embarked"] == 'C'].head(10)

#  Görev 8:  embarked değeri S olmayanların tüm bilgelerini gösteriniz.
df[df["embarked"] != 'S'].head(10)

# Görev 9:   Yaşı 30'dan küçük ve kadın olan yolcuların tüm bilgilerini gösteriniz.
df.loc[(df["age"] < 30) & (df["sex"] == "female")].head(30)

# Görev 10:  Fare'i 500'den büyük veya yaşı 70 den büyük yolcuların bilgilerini gösteriniz.
df.loc[(df["fare"] > 500) | (df["age"] > 70)].head(20)

# Görev 11: Her bir değişkendeki boş değerlerin toplamını bulunuz.
df.isnull().sum()

# Görev 12: who değişkenini dataframe'den düşürün.
df.drop("who", axis=1, inplace=True)

# Görev 13: deck değikenindeki boş değerleri deck değişkenin en çok tekrar eden değeri (mode) ile doldurunuz.
type(df["deck"].mode())
df["deck"].mode()[0]                  # en çok tekrar edeni .[0] sağladı
df["deck"].fillna(df["deck"].mode()[0], inplace=True)
df["deck"].isnull().sum()

# Görev 14: age değikenindeki boş değerleri age değişkenin medyanı ile doldurun.
type(df["age"].median())
df["age"].fillna(df["age"].median(), inplace=True)
df["age"].isnull().sum()
df.head()

# Görev 15: survived değişkeninin Pclass ve Cinsiyet değişkenleri kırılımınında sum, count, mean değerlerini bulunuz.
df = sns.load_dataset("titanic")
df.head()
df.shape

df.groupby(["pclass", "sex"]).agg({"survived" : ["sum", "count", "mean"]})

# Görev 16:  30 yaşın altında olanlar 1, 30'a eşit ve üstünde olanlara 0 vericek bir fonksiyon yazınız.
# Yazdığınız fonksiyonu kullanarak titanik veri setinde age_flag adında bir değişken oluşturunuz (apply ve lambda yapılarını kullanınız)
def alt_30(v):
    if v < 30:
        v = 0
    else:
        v = 1
    return v

df["age_flag"] = df["age"].apply(lambda x : alt_30(x))

# Görev 17: Seaborn kütüphanesi içerisinden Tips veri setini tanımlayınız.
dt = sns.load_dataset("tips")
dt.columns
dt.shape

# Görev 18: Time değişkeninin kategorilerine (Dinner, Lunch) göre total_bill  değerlerinin toplamını, min, max ve ortalamasını bulunuz.
dt.groupby("time").agg({"total_bill": ["sum", "min", "max", "mean"]})

# Görev 19: Günlere ve time göre total_bill değerlerinin toplamını, min, max ve ortalamasını bulunuz.
dt.groupby(["day", "time"]).agg({"total_bill": ["sum", "min", "max", "mean"]})

# Görev 20:Lunch zamanına ve kadın müşterilere ait total_bill ve tip  değerlerinin day'e göre toplamını, min, max ve ortalamasını bulunuz.
dt[(dt["time"] == "Lunch") & (dt["sex"] == "Female")].groupby("day").agg({"total_bill": ["sum", "min", "max", "mean"],
                                                                          "tip": ["sum", "min", "max", "mean"]})

# Görev 21: size'i 3'ten küçük, total_bill'i 10'dan büyük olan siparişlerin ortalaması nedir?
dt.loc[(dt["size"] < 3) & (dt["total_bill"] > 10), ["size", "total_bill"]].median()

# Görev 22: total_bill_tip_sum adında yeni bir değişken oluşturun. Her bir müşterinin ödediği totalbill ve tip in toplamını versin.
dt["total_bill_tip_sum"] = dt["total_bill"] + dt["tip"]
dt.head()

# Görev 23: total_bill_tip_sum değişkenine göre büyükten küçüğe sıralayınız ve ilk 30 kişiyi yeni bir dataframe'e atayınız.
new_df = dt.sort_values("total_bill_tip_sum", ascending=False)[:30]
new_df.shape