from typing import List, Tuple

section_assignment_pairs = open("puzzle_4/input.txt", "r")
section_assignment_pairs: list = section_assignment_pairs.read()
section_assignment_pairs = section_assignment_pairs.split("\n")


def get_number_of_useless_pairs(section_assignment_pairs: List[str]) -> Tuple[int]:
    number_of_useless_pairs = 0
    number_of_overlapped_pairs = 0

    for pair in section_assignment_pairs:
        section_1, section_2 = get_sections(pair)
        if section_1 & section_2 != set():
            number_of_overlapped_pairs += 1
        if section_1.issubset(section_2) or section_2.issubset(section_1):
            number_of_useless_pairs += 1
    return number_of_useless_pairs, number_of_overlapped_pairs


def get_sections(pair: List[str]) -> List[set]:
    range_2 = lambda a, b: range(a, b + 1)
    sections = [
        set(range_2(*[int(pos) for pos in section.split("-")]))
        for section in pair.split(",")
    ]

    return sections


print(get_number_of_useless_pairs(section_assignment_pairs))
