my_dict = {'Maria':1990,'Igor':1984,'Valeria':2014}
print(my_dict)
print(my_dict['Igor'])
my_dict['Irina'] = 1968
print(my_dict)
my_dict.update({'Sergei':1958, 'Evgeniy':1930})
print(my_dict)
deleted = my_dict.pop('Evgeniy')
print(deleted)
print(my_dict)

my_set = {28,'sky',3.14,'sky',628,28}
print(set(my_set))
my_set.add(('water',3))
my_set.discard(628)
print(my_set)