# Lesson learned from Course 1: Introduction to Data Science with Python
Sebagian catatan disini diambil dari [assignment week2](/course1-intro-to-data-science/week1/Assignment+2-mark1.ipynb)

Course singkat tentang Data Analysis dan Visualization: [datacarpentry.org](https://datacarpentry.org/python-ecology-lesson/). 
Ini bisa kita baca waktu naik kereta. Menjelaskan tentang penggunakan python hingga sqllite.
Baca selanjutnya di repo [Machine learning recipe](https://github.com/rajadavidh/machine-learning-recipe/blob/master/machine-learning.md)

## Perbedaan Series dan DataFrame - week2
Series --> Data 1 dimensi berbentuk array [(referensi)](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.max.html)
    
Contoh Series:
```python
pd.Series([4, 2, 0, 8], name='legs', index=idx)
```
    
DataFrame --> Data 2 dimensi berbentuk tabel [(referensi)](https://www.geeksforgeeks.org/python-pandas-dataframe-max/)
    
Contoh DataFrame:
```python
df = pd.DataFrame({"A":[12, 4, 5, 44, 1], 
                   "B":[5, 2, 54, 3, 2], 
                   "C":[20, 16, 7, 3, 8],  
                   "D":[14, 3, 17, 2, 6]}) 
```

----

# Querying
## Cara terbaik dalam mengambil kolom atau baris data - [referensi](https://www.geeksforgeeks.org/indexing-and-selecting-data-with-pandas/)
TODO
Indexing adalah metode pemotongan data (slicing) dari tabel induk menjadi tabel dengan baris / kolom yang lebih sedikit.

Ada 4 metode indexing pada panda: 
* `Dataframe.[ ]` ; This function also known as indexing operator
* `Dataframe.loc[ ]` : This function is used for labels
* `Dataframe.iloc[ ]` : This function is used for positions or integer based
* `Dataframe.ix[ ]` : This function is used for both label and integer based

### 1. Contoh pemakaian Indexing Operator: `Dataframe.[ ]`
Fungsi `.loc` dan `.iloc` menggunakan indexing operator untuk mendapatkan hasil

```python
# importing pandas package 
import pandas as pd 
  
# making data frame from csv file 
data = pd.read_csv("nba.csv", index_col ="Name") 
  
# retrieving single column by indexing operator 
first = data["Age"] 

# retrieving multiple columns by indexing operator 
first = data[["Age", "College", "Salary"]]
```

### 2. Contoh pemakaian label: `Dataframe.loc[ ]`
Fungsi ini untuk memilih data berdasarkan label kolom atau label baris

```python
# importing pandas package 
import pandas as pd 
  
# making data frame from csv file 
data = pd.read_csv("nba.csv", index_col ="Name") 
  
# retrieving single row by loc method 
first = data.loc["Avery Bradley"] 
second = data.loc["R.J. Hunter"]
print(first, "\n\n\n", second) 

# retrieving multiple rows by loc method 
first = data.loc[["Avery Bradley", "R.J. Hunter"]] 
print(first) 
```

#### Untuk memilih baris dan kolom:
```
Dataframe.loc[["row1", "row2"], ["column1", "column2", "column3"]]
```

Contoh:
```python
import pandas as pd 
  
# making data frame from csv file 
data = pd.read_csv("nba.csv", index_col ="Name") 
  
# retrieving two rows and three columns by loc method 
first = data.loc[["Avery Bradley", "R.J. Hunter"], 
                   ["Team", "Number", "Position"]] 

print(first) 
```

#### Untuk memilih semua baris dan beberapa kolom
Pakai tanda `:`
```
Dataframe.loc[[:, ["column1", "column2", "column3"]]
```

Contoh:
```python
import pandas as pd 
  
# making data frame from csv file 
data = pd.read_csv("nba.csv", index_col ="Name") 
  
# retrieving all rows and some columns by loc method 
first = data.loc[:, ["Team", "Number", "Position"]] 

print(first) 
```

### 3. Contoh pemakaian posisi angka: `Dataframe.iloc[ ]`
Fungsi ini untuk memilih data berdasarkan posisi kolom atau baris. 
Posisi yang kita masukkan dalam bentuk integer atau bilangan bulat.

```python
import pandas as pd 
  
# making data frame from csv file 
data = pd.read_csv("nba.csv", index_col ="Name") 

# retrieving single row by iloc method  
row2 = data.iloc[3]  
print(row2) 

# retrieving multiple rows by iloc method  
row2 = data.iloc [[3, 5, 7]] 
print(row2) 

# retrieving two rows and two columns by iloc method
# ^ ini memilih beberapa kolom dan baris
row2 = data.iloc [[3, 4], [1, 2]] 
print(row2) 

# retrieving all rows and some columns by iloc method
# ^ ini memilih semua baris dan beberapa kolom
row2 = data.iloc [:, [1, 2]]
print(row2)
```

### 4. Contoh pemakaian label dan posisi angka: `Dataframe.ix[ ]`
Ini adalah fungsi awal pada panda. Kita bisa memilih antara index atau label bersamaan.

Walaupun fungsi ini mumpuni, tapi bisa menimbulkan kebingungan karena tidak eksplisit: 
karena ada kasus kalau sebuah label kolom yang format seharusnya adalah string, tapi justru ditulis dalam bentuk angka.
Ini membuat ambigu. Misal kolom 'Nama' malah ditulis kolom '2'.

Fungsi ini sudah di non-aktifkan pada panda versi terbaru.

```python
# importing pandas package 
import pandas as pd 
   
# making data frame from csv file 
data = pd.read_csv("nba.csv", index_col ="Name") 
   
# retrieving row by ix method 
first = data.ix["Avery Bradley"] 
print(first) 

# retrieving row by ix method 
first = data.ix[1] 
print(first) 
```

### 5. Kesimpulan
Dalam memilih baris dan kolom tergantung pada kasus mana yang cocok

Ini ada [jawaban dari Stackoverflow](https://stackoverflow.com/questions/17071871/select-rows-from-a-dataframe-based-on-values-in-a-column-in-pandas) yang bisa kita jadikan Cheatsheet:


## Duplikat hanya kolom - week2 - [referensi](https://stackoverflow.com/questions/34682828/extracting-specific-selected-columns-to-new-dataframe-as-a-copy)
```python
one_gold_countries = one_gold['ID'].copy() # Just copy 'ID' column --> failed when we add new 'Diff' column
one_gold_countries = one_gold[['ID']].copy() # Just copy 'ID' column
```

## Duplikasi tabel - [referensi](https://towardsdatascience.com/10-python-pandas-tricks-that-make-your-work-more-efficient-2e8e483808ba)
Misalkan ada tabel berikut:
```python
import pandas as pd
df1 = pd.DataFrame({ 'a':[0,0,0], 'b': [1,1,1]})
df2 = df1
df2['a'] = df2['a'] + 1
df1.head()
```
^ Tujuan awalnya kita mau `df2` mendapat hasil duplikasi dari `df1`. Tapi ternyata hasil `df1` juga ikut berubah ketika kita memodifikasi `df2`

Kalau kita mau memodifikasi tabel `df2` tanpa mengubah nilai `df1`, maka kita perlu memakai fungsi `copy()`

Contohnya berikut:
```python
df2 = df1.copy()
```
atau
```python
from copy import deepcopy
df2 = deepcopy(df1)
```

Baca juga: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html
> Whether a copy or a reference is returned for a setting operation, may depend on the context. This is sometimes called chained assignment and should be avoided. See Returning a View versus Copy.

## Sorting - week2
Referensi sorting:
* https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sort_values.html
* https://www.geeksforgeeks.org/python-pandas-dataframe-sort_values-set-1/
* https://datatofish.com/sort-pandas-dataframe/

## Mendapatkan nilai maximum: `nlargest()` vs `max()`
```python
%%timeit -n 10
# Langkah#3: Lakukan perhitungan selisih max dan min
diff = max_population - min_population
county['DiffPopulation'] = diff.abs()  # Pastikan hasilnya absolute berdasarkan soal
    
# Pakai `nlargest()`
max_diff_county = county.nlargest(1, 'DiffPopulation')['CTYNAME']

# Pakai `max()`
max_diff = diff.abs().max()
```
Hasilnya `nlargest()` lebih lambat daripada `max()`. Untuk periksa, gunakan `timeit`

## Logical operator in panda - [referensi](https://stackoverflow.com/questions/21415661/logical-operators-for-boolean-indexing-in-pandas)
```
exp1 & exp2                # Element-wise logical AND
exp1 | exp2                # Element-wise logical OR
~exp1                      # Element-wise logical NOT
    
(exp1) operator (exp2) --> Contoh: (df['col1'] == x) & (df['col2'] == y) 
```  

## Cara menemukan string dalam kolom
### Mencari string dengan fungsi `str.contains()` - [stackoverflow](https://stackoverflow.com/questions/11350770/select-by-partial-string-from-a-pandas-dataframe): dalam sini juga ada cara mencari dengan regex
```python
df[df['A'].str.contains("Hello|Britain")==True]
```
atau
```python
df.loc[:, df.columns.str.contains('a')]
```

### Mencari string dengan fungsi `str.match()` - [davidhamann.de](https://davidhamann.de/2017/06/26/pandas-select-elements-by-string/)
```python
df[df['model'].str.match('Mac')]
df[df['model'].str.contains('ac')]
```

Berdasarkan [dokumentasi](https://pandas.pydata.org/pandas-docs/stable/user_guide/text.html) fungsi `match()` lebih strict daripada fungsi `contains()`
 
### Mencari string dengan fungsi `filter()` - [referensi](https://stackoverflow.com/questions/11350770/select-by-partial-string-from-a-pandas-dataframe)
Selects rows which contain the word hello in their index label
```python
df.filter(like='hello', axis=0)  
```https://stackoverflow.com/questions/15705111/getting-string-from-pandas-series-and-dataframes-in-python

### Mencari string dengan fungsi `find()` - [referensi](https://www.geeksforgeeks.org/python-pandas-series-str-find/)
```python
## substring to be searched
sub ='a'

## Creating and passsing series to new column
data["Indexes"]= data["Name"].str.find(sub)
```

### Ternyata operasi SQL bisa kita operasikan melalui fungsi bawaan panda - week3