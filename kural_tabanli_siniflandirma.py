#############################################
# - Kural Tabanlı Sınıflandırma ile Potansiyel Müşteri Getirisi Hesaplama
#############################################
import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = pd.read_csv("datasets/persona.csv")
df.head(10)
df.info()

# Görev 1
# Soru 2: Kaç unique SOURCE vardır? Frekansları nedir?
df["SOURCE"].nunique()
df["SOURCE"].value_counts()
100 * df["SOURCE"].value_counts() / len(df)

# Soru 3 : Kaç unique PRICE vardır?
df["PRICE"].nunique()

#  Soru 4: Hangi PRICE'dan kaçar tane satış gerçekleşmiş?
df["PRICE"].value_counts()

# Soru 5: Hangi ülkeden kaçar tane satış olmuş?
df["COUNTRY"].value_counts()

# Soru 6: Ülkelere göre satışlardan toplam ne kadar kazanılmış?
df.groupby("COUNTRY").agg({"PRICE": "sum"})

# Soru 7: SOURCE türlerine göre satış sayıları nedir?
df.groupby("SOURCE").agg({"PRICE": "value_counts"})

# Soru 8: Ülkelere göre PRICE ortalamaları nedir?
df.groupby("COUNTRY").agg({"PRICE": "mean"})

# Soru 9: SOURCE'lara göre PRICE ortalamaları nedir?
df.groupby("SOURCE").agg({"PRICE": "mean"})

# Soru 10: COUNTRY-SOURCE kırılımında PRICE ortalamaları nedir?
df.groupby(["COUNTRY", "SOURCE"]).agg({"PRICE": "mean"})

# Görev 2:  COUNTRY, SOURCE, SEX, AGE kırılımında ortalama kazançlar nedir?
df.groupby(["COUNTRY", "SOURCE", "SEX", "AGE"]).agg({"PRICE": "mean"})

# Görev 3:  Çıktıyı PRICE’a göre sıralayınız.
agg_df = pd.DataFrame(df.groupby(["COUNTRY", "SOURCE", "SEX", "AGE"]).
                      agg({"PRICE": "mean"}).sort_values(by="PRICE", ascending=False))

# Görev 4: Indekste yer alan isimleri değişken ismine çeviriniz.
agg_df.reset_index(inplace=True)

# Görev 5:  Age değişkenini kategorik değişkene çeviriniz ve agg_df’e ekleyiniz.
agg_df["AGE_CAT"] = pd.cut(agg_df["AGE"], [-1, 19, 23, 30, 40, 70],
                           labels=["0_18", "19_23", "24_30", "31_40", "41_70"])

# Görev 6:  Yeni seviye tabanlı müşterileri (persona) tanımlayınız.
agg_df["customers_level_based"] = (agg_df[["COUNTRY", "SOURCE", "SEX", "AGE_CAT"]].
                                   agg(lambda x: '_'.join(x).upper(), axis=1))
# tekilleştirme
agg_df = pd.DataFrame(agg_df.groupby("customers_level_based").agg({"PRICE": "mean"}))
agg_df.reset_index(inplace=True)

agg_df["customers_level_based"].value_counts()   # tekilleştirmeyi kontrol edelim

# Görev 7:  Yeni müşterileri (personaları) segmentlere ayırınız.
# Yeni personaları PRICE’a göre 4 segmente ayırınız.
# Segmentleri SEGMENT isimlendirmesi ile değişken olarak agg_df’e ekleyiniz.
# Segmentleri betimleyiniz (Segmentlere göre group by yapıp price mean, max, sum’larını alınız).
agg_df["SEGMENT"] = pd.qcut(agg_df["PRICE"], 4, labels=["D", "C", "B", "A"])
agg_df.groupby("SEGMENT").agg({"PRICE": ["mean", "max", "sum"]})

# Görev 8: Yeni gelen müşterileri sınıflandırıp, ne kadar gelir getirebileceklerini tahmin ediniz.
# 35 yaşında ANDROID kullanan bir Fransız kadını hangi segmente aittir ve ortalama ne kadar gelir kazandırması beklenir?
new_user = "FRA_ANDROID_FEMALE_31_40"
agg_df[agg_df["customers_level_based"] == new_user]

