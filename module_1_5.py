# Онлайн-университет URBAN
# Практическое задание по теме: "Неизменяемые и изменяемые объекты. Кортежи"

immutable_var = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun', 7, True)
print(immutable_var)
#immutable_var[2] = 'Mon'
#print(immutable_var)
# Изменить значения элементов кортежа нельзя потому, что объект кортеж не поддерживает назначение элемента

mutable_list = ['Урок истории', 10, 00, True]
mutable_list[0] = 'Урок математики'
print(mutable_list)
