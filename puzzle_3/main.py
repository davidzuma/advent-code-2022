from typing import Tuple

rucksacks_file = open("puzzle_3/input.txt", "r")
rucksacks: list = rucksacks_file.read().split("\n")


def get_sum_of_priorities(rucksacks: list) -> int:
    get_priority = lambda x: get_rucksack_priorities(get_same_item(split_in_two(x)))
    sum_of_priorities = sum(map(get_priority, rucksacks))
    return sum_of_priorities


def split_in_two(rucksack: str) -> Tuple[int, int]:
    half = len(rucksack) // 2
    return rucksack[:half], rucksack[half:]


def get_same_item(rucksacks: Tuple[int, int]) -> str:
    rucksack_1, rucksack_2 = rucksacks
    same_item = list(set(rucksack_1) & set(rucksack_2))[0]
    return same_item


def get_rucksack_priorities(same_item: str) -> int:
    if same_item.isupper():
        score = ord(same_item) - 38
    else:
        score = ord(same_item) - 96
    return score


print(get_sum_of_priorities(rucksacks))
