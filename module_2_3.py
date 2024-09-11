# Онлайн-университет URBAN
# Домашняя работа по уроку "Стиль кода часть II. Цикл While."
# Задача "Нули ничто, отрицание недопустимо!"

my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index_ml = 0
item_ml = 0
len_ml = len(my_list)

while index_ml <  len_ml:
    item_ml = my_list[index_ml]
    index_ml = index_ml + 1
    if item_ml == 0:
        continue
    elif item_ml < 0:
        break
    else:
        print(item_ml)