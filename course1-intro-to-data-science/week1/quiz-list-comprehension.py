"""
Here, why don’t you try converting a function into a list comprehension.

def times_tables():
    lst = []
    for i in range(10):
        for j in range (10):
            lst.append(i*j)
    return lst

times_tables() == [???]
"""

# Solution
def times_tables():
    lst = []
    for i in range(10):
        for j in range (10):
            lst.append(i*j)
    return lst

times_tables() == [j*i for i in range(10) for j in range(10)]


"""
Here’s a harder question which brings a few things together.

Many organizations have user ids which are constrained in some way. 
Imagine you work at an internet service provider and the user ids are all two letters followed by two numbers 
(e.g. aa49). Your task at such an organization might be to hold a record on the billing activity for each possible user.

Write an initialization line as a single list comprehension which creates a list of all possible user ids. 
Assume the letters are all lower case.

lowercase = 'abcdefghijklmnopqrstuvwxyz'
digits = '0123456789'

answer = [???]
correct_answer == answer
"""

# Solution
lowercase = 'abcdefghijklmnopqrstuvwxyz'
digits = '0123456789'

correct_answer = [a+b+c+d for a in lowercase for b in lowercase for c in digits for d in digits]

correct_answer[:50] # Display first 50 ids
