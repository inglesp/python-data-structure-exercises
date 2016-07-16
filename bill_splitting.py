# This program reports how much individuals should pay for their order at
# dinner.
#
# Usage:
#
# $ python bill_splitting.py [name]
#
# For instance:
#
# $ python bill_splitting.py Tom
# Tom should pay 38.55
#
# or:
#
# $ python bill_splitting.py Tim
# Tim did not have dinner

bill_items = [
    ['Tom', 'Calamari', 6.00],
    ['Tom', 'American Hot', 11.50],
    ['Tom', 'Chocolate Fudge Cake', 4.45],
    ['Clare', 'Bruschetta Originale', 5.35],
    ['Clare', 'Fiorentina', 10.65],
    ['Clare', 'Tiramasu', 4.90],
    ['Rich', 'Bruschetta Originale', 5.35],
    ['Rich', 'La Reine', 10.65],
    ['Rich', 'Honeycomb Cream Slice', 4.90],
    ['Rosie', 'Garlic Bread', 4.35],
    ['Rosie', 'Veneziana', 9.40],
    ['Rosie', 'Tiramasu', 4.90],
]

print('There are {} items on the bill'.format(len(bill_items)))


# TODO:
# * Implement the program as described in the comments at the top of the file.

# TODO (extra):
# * Change the program so that it additionally reports a breakdown of what each
#   person had to eat.
# * Change the program so that if it is called without arguments, a table of
#   how much everybody should pay is displayed
