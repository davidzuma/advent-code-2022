from typing import Tuple, Iterable

with open("puzzle_3/input.txt", "r") as file:
    rucksacks: list = file.read().split("\n")
rucksacks_packed = [rucksacks[idx : idx + 3] for idx in range(0, len(rucksacks), 3)]


def get_sum_of_priorities(rucksacks: list, rucksacks_packed: list) -> int:
    get_priority = lambda x: get_rucksack_priorities(get_same_item(split_in_two(x)))
    get_priority_packed = lambda x: get_rucksack_priorities(get_same_item(x))
    sum_of_priorities = sum(map(get_priority, rucksacks))
    sum_of_priorities_packed = sum(map(get_priority_packed, rucksacks_packed))
    return sum_of_priorities, sum_of_priorities_packed


def split_in_two(rucksack: str) -> Tuple[str, str]:
    half = len(rucksack) // 2
    return rucksack[:half], rucksack[half:]


def get_same_item(rucksacks: Iterable) -> str:
    rucksacks_unique_items: Iterable[set] = [set(rucksack) for rucksack in rucksacks]
    same_item = list(set.intersection(*rucksacks_unique_items))[0]
    return same_item


def get_rucksack_priorities(same_item: str) -> int:
    if same_item.isupper():
        score = ord(same_item) - 38
    else:
        score = ord(same_item) - 96
    return score


print(get_sum_of_priorities(rucksacks, rucksacks_packed))
