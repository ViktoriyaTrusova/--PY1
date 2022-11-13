from random import  random
def get_unique_list_numbers() -> list[int]:
    size = 15
    max = 10
    min = -10
    list_unique_numbers = []
    while len(list_unique_numbers) != size:
        random_val = random(max_, min_)
        if random_val not in list_unique_numbers:
            list_unique_numbers.append(random_val)
    return list_unique_numbers

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
