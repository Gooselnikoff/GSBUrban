# Онлайн-университет URBAN
# Самостоятельная работа по уроку "Произвольное число параметров".
# Цель: закрепить знание использования параметров *args/ **kwargs на практике.
# Задача "Однокоренные"

def single_root_words(root_word, *other_words) :
    root_word_up = root_word.upper()
    same_words = []
    for one_other_word in other_words:
        one_other_word_up = one_other_word.upper()
        if one_other_word_up.count(root_word_up) or root_word_up.count(one_other_word_up):
            same_words.append(one_other_word)
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
result3 = single_root_words('enter', 'entering', 'entered', 'enters', 'enterst')
print(result1)
print(result2)
print(result3)

