#############################################
# PANDAS
#############################################

# Toplulaştırma ve Gruplama (Aggregation & Grouping)
# Apply ve Lambda
# Birleştirme (Join) İşlemleri


#############################################
# Toplulaştırma ve Gruplama (Aggregation & Grouping)
#############################################
# - Toplulaştırma fonksiyonları -
# - count()
# - first()
# - last()
# - mean()
# - median()
# - min()
# - max()
# - std()
# - var()
# - sum()
# - pivot table

import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns', None)
df = sns.load_dataset('titanic')
df.head()

df["age"].mean()     # herkesin yaş ortalaması

# - Gruplama -
df.groupby("sex")["age"].mean()     # cinsiyet kırılımında yaş değişkeninin ortalaması; erkek ve kadın ayrı hesaplar
# df.groupby("x") x'e göre veriyi gruplandır

df.groupby("sex").agg({"age": "mean"})  # yukarıdaki ile aynı çıktıyı verir ama type dataframe'dir
df.groupby("sex").agg({"age": ["mean", "sum"]})
# cinsiyet kırılımında yaş değişkeninin hem ortalamasını hem de toplamını verir

df.groupby("sex").agg({"age": ["mean", "sum"],
                       "embark_town": "count"})   # ek olarak bindiği yerin frekans bilgisini verir

# önce cinsiyete göre sonra limana binişe göre kırıp; buna göre yaşın ve survived değişkeninin ortalaması
df.groupby(["sex", "embark_town"]).agg({"age": ["mean"],
                                        "survived": "mean"})

df.groupby(["sex", "embark_town", "class"]).agg({"age": ["mean"],
                                                 "survived":"mean"}) # ayrıca class bilgisi eklenmiş

df.groupby(["sex", "embark_town", "class"]).agg({"age": ["mean"],
                                                 "survived": "mean",
                                                 "sex": "count"})    # cinsiyete göre saydırıp kaç kişi olduğunu görürüz


#############################################
# Pivot Table
#############################################
# Pivot tablolar, büyük veri kümelerini özetlemek, analiz etmek ve anlamlı bilgiler çıkarmak için kullanılır.
# Özellikle veri analizinde ve raporlama süreçlerinde oldukça faydalıdır.

# Veri Filtreleme ve Gruplama
# Belirli kriterlere göre verileri filtreleyebilir ve gruplandırabilirsiniz.
# Örneğin, belirli bir tarihler arasında yapılan satışları
# veya belirli ürün kategorileri için verileri görüntüleyebilirsiniz.
#
# Dinamik Veri Analizi
# Pivot tablolar, verilerinizi dinamik olarak analiz etmenize olanak tanır.
# Sütunları ve satırları sürükleyip bırakarak, verilerinizi farklı açılardan inceleyebilirsiniz.
#
# Görselleştirme
# Pivot tablolar, grafikler ve şemalar gibi görselleştirme araçlarıyla entegre çalışabilir.
# Bu da verilerinizi görsel olarak analiz etmenizi ve sunmanızı kolaylaştırır.

df.pivot_table("survived", "sex", "embarked") # ön tanımı ortalama verir, yani bu hali
# birinci argüman (values): kesişimlerde neyi görmek istiyorsun
# ikinci argüman (index): satırda hangi değişkeni görmek istersin
# üçüncü argüman (columns): sütunda hangi değişkeni görmek istersin

df.pivot_table("survived", "sex", "embarked", aggfunc="std") # bu kesişimdeki değişkenlerin standart sapmasını hesapladı
df.pivot_table("survived", "sex", ["embarked", "class"])

# cut ve qcut fonk'ları sayısal değişkenleri kategorik değişkene çevirmek için kullanılır
df["new_age"] = pd.cut(df["age"], [0, 10, 18, 25, 40, 90])
df.pivot_table("survived", "sex", "new_age")

df.pivot_table("survived", "sex", ["new_age", "class"])

# pd.cut
# Amaç: Verileri belirli aralıklara bölmek.
# Kullanım: pd.cut, bir veri serisini eşit aralıklara veya belirli sınırlarla tanımlanmış aralıklara böler.
# Kullanım Alanı: Veriyi belirli sayısal aralıklara ayırmak istediğinizde kullanılır.

# pd.qcut
# Amaç: Verileri eşit frekans aralıklarına bölmek.
# Kullanım: pd.qcut, bir veri serisini belirli yüzdelik dilimlere (percentiles) göre böler.
# Bu, her bir kategoride yaklaşık olarak eşit sayıda veri noktası olmasını sağlar.
# Kullanım Alanı: Veriyi eşit büyüklükteki gruplara ayırmak istediğinizde kullanılır.