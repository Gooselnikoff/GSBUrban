# Онлайн-университет URBAN
# Практическое задание по теме: "Словари и множества"
#

# Работа со словарями:
my_dict = {'Anton':1999, 'Nikita':2000, 'Natalia':1997, 'Vladimir':2001}
print('Dict:', my_dict)
print('Existing value:', my_dict.get('Nikita'))
print('Not existing value:', my_dict.get('Serega'))
my_dict.update({'Stas': 2002, 'Oleg': 2000})
print('Modified dictionary:' , my_dict)
a = my_dict.pop('Anton')
print('Deleted value:', a)
print('Modified dictionary:', my_dict)

# Работа с множествами:
my_set = {1, 'string', 1, 2, 3, 4, True, 5, False, (1, 2, 3), 1, 'string', 1, 'string', 1, 2, 3, 4, True, 5, False, (1, 2, 3), 1, 2, 3, 4, True, 5, False, (1, 2, 3)}
print('Set:', my_set)
my_set.add(10)
my_set.add(11)
my_set.discard(5)
print('Modified set:', my_set)