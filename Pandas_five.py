#############################################
# PANDAS
#############################################

# Birleştirme (Join) İşlemleri

#############################################
# Birleştirme (Join) İşlemleri
#############################################
import numpy as np
import pandas as pd
m = np.random.randint(1, 30, size=(5, 3))
df1 = pd.DataFrame(m, columns=["var1", "var2", "var3"])
df2 = df1 + 99


# İki yöntem bulunur
# - concat -
pd.concat([df1, df2])   # alt alta birleştirme yapar;
pd.concat([df1, df2], axis=1)  # axis=1 yaparsan yan yana birleştirir

# index bilgisini düzeltmek için
pd.concat([df1, df2], ignore_index=True)  # indexler lineer büyür


# - Merge -
df1 = pd.DataFrame({'employees': ['john', 'dennis', 'mark', 'maria'],
                    'group': ['accounting', 'engineering', 'engineering', 'hr']})

df2 = pd.DataFrame({'employees': ['mark', 'john', 'dennis', 'maria'],
                    'start_date': [2010, 2009, 2014, 2019]})

pd.merge(df1, df2)                  # hangi değişkene göre birleştirmesi gerektiğini kendisi bilir
pd.merge(df1, df2, on="employees")  # özellikle birleştirme değişkeni seçmek için "on" kullanılır

# Amaç: Her çalışanın müdürünün bilgisine erişmek istiyoruz.
df3 = pd.merge(df1, df2)

df4 = pd.DataFrame({'group': ['accounting', 'engineering', 'hr'],
                    'manager': ['Caner', 'Mustafa', 'Berkcan']})

pd.merge(df3, df4)

