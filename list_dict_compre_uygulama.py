

#  1 -- Bir veri setindeki değişken isimlerini değiştirmek

import seaborn as sns                   # kütüphane import etme yöntemi
df = sns.load_dataset("car_crashes")
df.columns



A = []                        # Klasik yöntem
for col in df.columns:
    A.append(col.upper())
df.columns = A


# Comprehension
df = sns.load_dataset("car_crashes")
df.columns = [col.upper() for col in df.columns]


# 2 -- İsminde "INS" olan değişkenlerin başına FLAG, diğerlerine NO_FLAG eklemek istiyoruz.
B = ["FLAG_" + col if "INS" in col else "NO_FLAG_" + col for col in df.columns]



# 3 -- Amaç: key'i string, value'su aşağıdaki gibi bir liste olan sözlük oluşturmak.
#            bu işlemi sadece sayısal değişkenler için yapmak istiyoruz


num_cols = [col for col in df.columns if df[col].dtype != "O"] # data setindeki(df) sayısal(numeric) değişkenleri seçtik
soz = {}                                                       # büyük o yani -> object
agg_list = ["mean", "min", "max", "sum"]

for col in num_cols:
    soz[col] = agg_list

# kısa yol
new_dict = {col: agg_list for col in num_cols}
# burada key kısımları değişir, value'ler sabit