# Онлайн-университет URBAN
# Домашняя работа по уроку "Пространство имён"

calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(string):
    low_string = string.lower()
    upp_string = string.upper()
    len_string = len(string)
    count_calls()
    return len_string, low_string, upp_string

def is_contains(string, my_list):
    string = string.upper()
    for i in range(len(my_list)):
        my_list[i] = my_list[i].upper()
        if string == my_list[i]:
            str_is_contains = True
        else:
            str_is_contains = False
    count_calls()
    return str_is_contains


print(string_info('University'))
print(string_info('Urban'))
print(string_info('BaNaN'))
print(is_contains('Urban', ['University', 'ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('Cycle', ['recycling', 'cyclic'])) # No matches
print(calls)