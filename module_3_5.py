# Онлайн-университет URBAN
# Самостоятельная работа по уроку "Рекурсия"
# Цель: применить знания о рекурсии в решении задачи.
# Задача "Рекурсивное умножение цифр" (кроме 0)

def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    global recursion_level
    if len(str_number) > 1:
        recursion_level += 1
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        if first == 0:
            if recursion_level == 0:
                print('В числе нет цифр болше нуля.')
                return 0
            else:
                return 1
        else:
            return first

recursion_level = 0
print(get_multiplied_digits(0))
print(get_multiplied_digits(7))
print(get_multiplied_digits(10))
print(get_multiplied_digits(200))
print(get_multiplied_digits(40203))
print(get_multiplied_digits(402030))
print(get_multiplied_digits(402035))
print(get_multiplied_digits(4020355))
print(get_multiplied_digits(700007))
