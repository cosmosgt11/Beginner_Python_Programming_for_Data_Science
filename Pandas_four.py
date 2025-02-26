#############################################
# PANDAS
#############################################

# Apply ve Lambda
# Birleştirme (Join) İşlemleri


#############################################
# Apply ve Lambda
#############################################

# Pandas apply fonksiyonu, bir DataFrame veya Series'in her bir öğesine belirli bir fonksiyon uygulamak için kullanılır.
# Bu, verilerinizi hızlı ve esnek bir şekilde işleyebilmenizi sağlar.
# For veya benzeri döngüler yazmaktan kurtarır

# Lambda fonksiyonları (veya anonim fonksiyonlar), bir veya daha fazla girdi alan ve bir sonuç döndüren küçük,
# tek satırlık fonksiyonlardır. Lambda ifadeleri genellikle kısa ve basit işlemler için kullanılır.
import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset('titanic')
df.head()

df["age2"] = df["age"]*2
df["age3"] = df["age"]*5

(df["age"]/10).head()
(df["age2"]/10).head()
(df["age3"]/10).head()

# değişkenlere fonksiyon uygulamak
for col in df.columns:
    if "age" in col:
        print(col)

for col in df.columns:
    if "age" in col:
        print((df[col]/10).head())

for col in df.columns:
    if "age" in col:
        df[col] = df[col]/10

# APPLY ve LAMBDA ile değişkenlere fonksiyon uygulamak
df[["age", "age2", "age3"]].apply(lambda x: x/10).head()

df.loc[:, df.columns.str.contains("age")].apply(lambda x: x/10).head()

df.loc[:, df.columns.str.contains("age")].apply(lambda x: (x - x.mean()) / x.std()).head() # standartlaştırma

df.loc[:, df.columns.str.contains("age")] = df.loc[:, df.columns.str.contains("age")].apply(lambda x: (x - x.mean()) / x.std()).head()



