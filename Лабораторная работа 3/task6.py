list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO Оформить решение
for i, val in enumerate(list_numbers):
    if val == max(list_numbers):
        indx_max = i
        break  # без брейка потенциально выдаст индекс последнего максимального

list_numbers[indx_max], list_numbers[-1] = list_numbers[-1], list_numbers[indx_max]
print(list_numbers)
