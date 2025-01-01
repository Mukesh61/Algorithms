"""
find mid point using mid = (lower_limit + upper_limit)//2
if target number not in mid then there are two posibility, if target number is greater than or lower than mid.

1. lower_limit | target number | mid -1 | mid | upper_limit
since we already checked the mid so we can exclude everything >= mid so change the upper limit.
upper_limit = mid -1

2. lower_limit | mid | mid + 1 | target number | upper_limit
since target number is greater than mid, so exclude everything <= mid by changing lower_limit.
lower_limit = mid + 1 

This way at last it will reach to a single number with position like
4 | 5
lower_limit = 4, upper_limit = 5
so mid = (4 + 5)//2 = 4
new limit will be

lower_limit = mid +1 = 5, upper_limit = 5, if target in the 5th position 
otherwise lower_limit > upper_limit means we can searched everything in the list. 
so we can use lower_limit <= upper_limit in the while loop.

"""
import random


def binary_search(input_data, random_list):
    lower_limit = 0
    upper_limit = len(random_list) - 1

    while lower_limit <= upper_limit:
        mid = (lower_limit + upper_limit)//2
        if random_list[mid] == input_data:
            return "Found"
        elif random_list[mid] < input_data:
            lower_limit = mid + 1
        elif random_list[mid] > input_data:
            upper_limit = mid - 1

    return "Not Found"

input_data = 1

while input_data:
    input_data = int(input("enter a number: "))
    random_list = [random.randint(1, 100) for i in range(20)]
    random_list.sort()

    result = binary_search(input_data, random_list)
    print(f"{result} in {random_list}")
