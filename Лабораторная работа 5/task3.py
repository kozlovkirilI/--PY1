from random import sample

start_ = -10
end_ = 10
k_ = 15


def get_unique_list_numbers(start, end, k) -> list[int]:
    return sample(range(start, end + 1), k)


list_unique_numbers = get_unique_list_numbers(start_, end_, k_)
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
