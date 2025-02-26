
import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = pd.read_excel("datasets/miuul_gezinomi.xlsx")
df = df.drop_duplicates()
df.head(10)
df.info()

# GÖREV 1
# Soru 2 :Kaç unique şehir vardır? Frekansları nedir?
df["SaleCityName"].nunique()
df["SaleCityName"].value_counts()                   # frekansları
100 * df["SaleCityName"].value_counts() / len(df)   # yüzdelik değerleri

# Soru 3 : Kaç unique Concept vardır?
df["ConceptName"].nunique()

# Soru 4 : Hangi Concept’den kaçar tane satış gerçekleşmiş?
df["ConceptName"].value_counts()

# Soru 5 : Şehirlere göre satışlardan toplam ne kadar kazanılmış?
df.groupby("SaleCityName").agg({"Price": "sum"})

# Soru 6 : Concept türlerine göre ne kadar kazanılmış?
df.groupby("ConceptName").agg({"Price": "sum"})

# Soru 7 : Şehirlere göre PRICE ortalamaları nedir?
df.groupby("SaleCityName").agg({"Price": "mean"})

# Soru 8 : Conceptlere göre PRICE ortalamaları nedir?
df.groupby("ConceptName").agg({"Price": "mean"})

# Soru 9 : Şehir-Concept kırılımında PRICE ortalamaları nedir?
df.groupby(["SaleCityName", "ConceptName"]).agg({"Price": "mean"})


# GÖREV 2 : "SaleCheckInDayDiff" değişkenini kategorik bir değişkene çeviriniz.
df["EB_Score"] = pd.cut(df["SaleCheckInDayDiff"], [-1, 7, 30, 90, 633],
                                 labels=["Last Minuters", "Potential Planners", "Planners", "Early Bookers"])

# Görev 3:  COUNTRY, SOURCE, SEX, AGE kırılımında ortalama kazançlar nedir?
# 1
df.groupby(["SaleCityName", "ConceptName", "EB_Score"]).agg({"Price": ["mean", "count"]})
# 2
df.groupby(["SaleCityName", "ConceptName", "Seasons"]).agg({"Price": ["mean", "count"]})
# 3
df.groupby(["SaleCityName", "ConceptName", "CInDay"]).agg({"Price": ["mean", "count"]})

# Görev 4:  City-Concept-Season kırılımının çıktısını PRICE'a göre sıralayınız.
agg_df = (df.groupby(["SaleCityName", "ConceptName", "Seasons"]).agg({"Price": "mean"})
          .sort_values(by="Price", ascending=False))

# Görev 5:  Indekste yer alan isimleri değişken ismine çeviriniz.
agg_df.reset_index(inplace=True)

# Görev 6:  Yeni seviye tabanlı müşterileri (persona) tanımlayınız.
# Önceki soruda elde edeceğiniz çıktıdaki gözlemleri bir araya getirerek
# sales_level_based değişkenini oluşturmanız gerekmektedir.
agg_df['sales_level_based'] = agg_df[["SaleCityName", "ConceptName", "Seasons"]].agg(lambda x: '_'.join(x).upper(), axis=1)

# Görev 7:  Yeni müşterileri (personaları) segmentlere ayırınız.
# Yeni personaları PRICE’a göre 4 segmente ayırınız.
# Segmentleri SEGMENT isimlendirmesi ile değişken olarak agg_df’e ekleyiniz.
# Segmentleri betimleyiniz (Segmentlere göre group by yapıp price mean, max, sum’larını alınız).
agg_df["SEGMENT"] = pd.qcut(agg_df["Price"], 4, labels=["D", "C", "B", "A"])
agg_df.groupby("SEGMENT").agg({"Price": ["mean", "max", "sum"]})

# Görev 8: Yeni gelen müşterileri sınıflandırıp, ne kadar gelir getirebileceklerini  tahmin ediniz.
agg_df.sort_values(by="Price")

new_user = "ANTALYA_HERŞEY DAHIL_HIGH"
agg_df[agg_df["sales_level_based"] == new_user]