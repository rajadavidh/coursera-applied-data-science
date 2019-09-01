import pandas as pd

# DataFrame Data structure
"""
For the purchase records from the pet store, how would you get a list of all items which had been purchased
(regardless of where they might have been purchased, or by whom)?
"""

purchase_1 = pd.Series({'Name': 'Chris',
                        'Item Purchased': 'Dog Food',
                        'Cost': 22.50})
purchase_2 = pd.Series({'Name': 'Kevyn',
                        'Item Purchased': 'Kitty Litter',
                        'Cost': 2.50})
purchase_3 = pd.Series({'Name': 'Vinod',
                        'Item Purchased': 'Bird Seed',
                        'Cost': 5.00})

df = pd.DataFrame([purchase_1, purchase_2, purchase_3], index=['Store 1', 'Store 1', 'Store 2'])

# Your code here
df.loc[:, 'Item Purchased']

# Solution
df['Item Purchased']


"""
For the purchase records from the pet store, how would you update the DataFrame, 
applying a discount of 20% across all the values in the 'Cost' column?
"""

purchase_1 = pd.Series({'Name': 'Chris',
                        'Item Purchased': 'Dog Food',
                        'Cost': 22.50})
purchase_2 = pd.Series({'Name': 'Kevyn',
                        'Item Purchased': 'Kitty Litter',
                        'Cost': 2.50})
purchase_3 = pd.Series({'Name': 'Vinod',
                        'Item Purchased': 'Bird Seed',
                        'Cost': 5.00})

df = pd.DataFrame([purchase_1, purchase_2, purchase_3], index=['Store 1', 'Store 1', 'Store 2'])

# Your answer here
discount = df.copy()
discount['Cost'] = discount['Cost'] * 0.8

# Solution
df['Cost'] *= 0.8
print(df)


# Querying DataFrame
"""
Write a query to return all of the names of people who bought products worth more than $3.00.
"""
purchase_1 = pd.Series({'Name': 'Chris',
                        'Item Purchased': 'Dog Food',
                        'Cost': 22.50})
purchase_2 = pd.Series({'Name': 'Kevyn',
                        'Item Purchased': 'Kitty Litter',
                        'Cost': 2.50})
purchase_3 = pd.Series({'Name': 'Vinod',
                        'Item Purchased': 'Bird Seed',
                        'Cost': 5.00})

df = pd.DataFrame([purchase_1, purchase_2, purchase_3], index=['Store 1', 'Store 1', 'Store 2'])

# Your code here
name = df['Name'][df['Cost'] > 3]

# Solution
df['Name'][df['Cost']>3]