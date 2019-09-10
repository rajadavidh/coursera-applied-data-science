import pandas as pd
"""
Here are two DataFrames, products and invoices. 

The product DataFrame has an identifier and a sticker price.
The invoices DataFrame lists the people, product identifiers, and quantity.

Assuming that we want to generate totals, how do we join these two DataFrames together so that
we have one which lists all of the information we need?

products DataFrame:

            |   Price	|   Product
------------|-----------|-------------
Product ID  |           |
4109	    |   5.0	    |   Sushi Roll
1412	    |   0.5	    |   Egg
8931	    |   1.5	    |   Bagel

invoices DataFrame:

    |   Customer	|   Product ID	|   Quantity
----|---------------|---------------|---------------
0	|   Ali	        |   4109	    |   1
1	|   Eric	    |   1412	    |   12
2	|   Ande	    |   8931	    |   6
3	|   Sam	        |   4109	    |   2

"""
# products and invoices are already initalized.

# Untuk menyelesaikan ini, kita lakukan left JOIN. Alasannya:
# 1. Right atau Left JOIN pada dasarnya bisa kita tukar2. Baca course SQL dari Udacity
# 2. Karena soalnya meminta kita untuk mendapatkan jumlah total, maka tabel invoice kita letakkan di sebelah kiri
answer = pd.merge(invoices, products, how='left', left_on='Product ID', right_index=True)

answer = pd.merge(products, invoices, how='left', left_index=True, right_on='Product ID')  # Ubah posisi tabel menyesuaikan jawaban

"""
Hasil jawabanku:

  Customer  Product ID  Quantity  Price     Product
0      Ali        4109         1    5.0  Sushi Roll
1     Eric        1412        12    0.5         Egg
2     Ande        8931         6    1.5       Bagel
3      Sam        4109         2    5.0  Sushi Roll

Hasil correct_answer justru meletakkan tabel products di sebelah kiri:
   Price     Product Customer  Product ID  Quantity
0    5.0  Sushi Roll      Ali        4109         1
3    5.0  Sushi Roll      Sam        4109         2
1    0.5         Egg     Eric        1412        12
2    1.5       Bagel     Ande        8931         6
"""

answer == correct_answer

# Solution
print(pd.merge(products, invoices, left_index=True, right_on='Product ID'))  # Solusinya gak pake argument `how`
