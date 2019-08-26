"""
Here is a list of faculty teaching this MOOC.
Can you write a function and apply it using map() to get a list of all faculty titles and last names
(e.g. ['Dr. Brooks', 'Dr. Collins-Thompson', …]) ?

people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']

def split_title_and_name(person):
    return #Your answer here

list(map(split_title_and_name))
"""

# My attempt
people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']

def split_title_and_name(person):
    title = person.split(' ')[0]
    lastname = person.split(' ')[2]
    return title+lastname

list(map(split_title_and_name, people))

# Solution
people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']

def split_title_and_name(person):
    title = person.split()[0]
    lastname = person.split()[-1]
    return '{} {}'.format(title, lastname)

list(map(split_title_and_name, people))
