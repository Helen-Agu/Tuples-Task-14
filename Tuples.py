print("Hello, El!")

# Creating tuples
tuple1 = ('Tola', 'Nkechi', 'Deji', 
          'Ronke', 'Onyedika', 'Olaedo')
tuple2 = ('Bose', 'Amaka', 'Mustapha')

# joining 2 tuples - Concatenation operator (+)
print(tuple1 + tuple2)

# membership operator
print('Bose' in tuple1)
print('Tola' not in tuple2)

# number of items in the tuple
print(len(tuple1))
print(len(tuple2))

# Repetition operator (*)
print(tuple2*3)

# index
print (tuple1.index('Nkechi'))
print (tuple1.index('Olaedo'))
print (tuple2.index('Mustapha'))

