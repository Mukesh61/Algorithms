"""
Selection Sort:
1. Go through the entire list and find the min value
2. keep min value in the first index

This way we got the first min value in the first index.
now repeat this to get 2nd min value until entire list is sorted.

"""
def selection_sort(list_of_item):
    current_index = 0
    end_index = len(list_of_item) - 1
    while current_index <= end_index:
        min_index, min_value = find_min(list_of_item, current_index, end_index)
        current_value = list_of_item[current_index]
        if min_index != current_index:
            list_of_item[current_index] = min_value
            list_of_item[min_index] = current_value
        current_index += 1
    return list_of_item

def find_min(list_of_item, start_index, end_index):
    min_value = list_of_item[start_index]
    min_index = start_index

    while start_index <= end_index:
        value = list_of_item[start_index]
        if value < min_value:
            min_value = value
            min_index = start_index
        start_index += 1

    return min_index, min_value



list_of_item = [4, 3, 1, 8, 56, 88, 79]
print(f"Before sort: {list_of_item}")

list_of_item = selection_sort(list_of_item)
print(f"After sort : {list_of_item}")
