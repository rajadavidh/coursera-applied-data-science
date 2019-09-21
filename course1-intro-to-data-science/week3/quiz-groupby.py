import pandas as pd
"""
                       Category  Quantity  Weight (oz.)
Item                                                   
Pack                       Pack         1          33.0
Tent                    Shelter         1          80.0
Sleeping Pad              Sleep         1          27.0
Sleeping Bag              Sleep         1          20.0
Toothbrush/Toothpaste    Health         1           2.0
Sunscreen                Health         1           5.0
Medical Kit              Health         1           3.7
Spoon                   Kitchen         1           0.7
Stove                   Kitchen         1          20.0
Water Filter            Kitchen         1           1.8
Water Bottles           Kitchen         2          35.0
Pack Liner              Utility         1           1.0
Stuff Sack              Utility         1           1.0
Trekking Poles          Utility         1          16.0
Rain Poncho            Clothing         1           6.0
Shoes                  Clothing         1          12.0
Hat                    Clothing         1           2.5

Looking at our backpacking equipment DataFrame, suppose we are interested in finding our total weight for each category. 

Use groupby to group the dataframe, and apply a function to calculate the total weight (Weight x Quantity) by category.
"""
print(df)

# Your code here

# My attempt#1 (Belum berhasil)
# Atur kolom `Category` sebagai index
# Karena kita akan menggunakan fungsi `total_weight` sebagai input pada fungsi `.groupby()`
df = df.set_index('Category')

# Tulis fungsi menghitung berat total
# Kita memakai `item` sebagai input karena kita telah mengatur kolom `Category` sebagai index
# sehingga `item[1]` adalah kolom Weight dan `item[2]` adalah kolom Quantity
def total_weight(item):
    total = item[1] * item[2]
    return total

# Lakukan `groupby` berdasarkan kategori
for group, frame in df.groupby(total_weight):
    print('Category ' + group + ' have a total weight ' + str(total))

# Solusi diatas belum berhasil:
# Aku kira `item[1]` adalah kolom Weight dan `item[2]` adalah kolom Quantity.
# Tapi ternyata `item[1]` justru adalah huruf pertama dari index dan `item[2]` adalah huruf kedua dari index

# ----------------------------

# My attempt#2 (Belum berhasil)
# Tulis fungsi menghitung berat total
def total_weight(weight, qty):
    total = weight * qty
    return total

# Lakukan `groupby` berdasarkan kategori
for group, frame in df.groupby('Category'):
    total = total_weight(frame['Weight (oz.)'], frame['Quantity'])
    print('Category ' + group + ' have a total weight ' + str(total))

# Solusi diatas belum berhasil:
# Ternyata `frame['Weight (oz.)']` memberikan hasil dalam format dataframe yang
# gak bisa kita jadikan sebagai input untuk operasi perkalian dalam fungsi `total_weight`

# ----------------------------

# Solution
print(df.groupby('Category').apply(lambda df,a,b: sum(df[a] * df[b]), 'Weight (oz.)', 'Quantity'))

# Or alternatively without using a lambda:
def totalweight(df, w, q):
       return sum(df[w] * df[q])

print(df.groupby('Category').apply(totalweight, 'Weight (oz.)', 'Quantity'))