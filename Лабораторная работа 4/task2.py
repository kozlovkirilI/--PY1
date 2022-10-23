# TODO посчитать количество каждой буквы в строке в аргументе str_
def get_count_char(str_):
    dict_ = {}
    for char in str_.lower(): 
        if not char.isalpha():
            continue

        dict_[char] = dict_.get(char, 0) + 1

    return dict_


def get_percentage_char(dict_):
    total_amount = sum(dict_.values())
    new_dict = {key: dict_[key] / total_amount for key in dict_}
    return new_dict


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))

