list_numbers = [2, 90, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

max_element_index = list_numbers[0]

for key, value in enumerate(list_numbers):
    if value >= max_element_index:
        max_element_index = value
        keyword = key

list_numbers[keyword],list_numbers[-1] = list_numbers[-1], max_element_index

print(list_numbers)  # Ответ [2, 90, -2, 8, -36, -44, -1, -85, -14, 25, -22, -90, -100, -8, 38, -92, -45, 67, 53, 90]
