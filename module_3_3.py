# Онлайн-университет URBAN
# Самостоятельная работа по уроку "Распаковка позиционных параметров".
# Задача "Распаковка"

def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)


# 1.Функция с параметрами по умолчанию
print_params()
print_params(True, 5, 'параметр')
print_params(b=25)
print_params(c=(3, True, 'Функция'))


# 2.Распаковка параметров
values_list = ['Проверка', False, 29]
print_params(*values_list)
values_list = [3, 1]
print_params(5, *values_list)

values_dict = {'a':72, 'b':'Тюмень', 'c': False}
print_params(**values_dict)

