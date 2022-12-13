import pytest
from main import split_in_two, get_same_item, get_rucksack_priorities

RUCKSACK = "FzQrhQpJtJMFzlpplrTWjTnTTrjVsVvvTnTs"
RUCKSACKS = ("FzQrhQpJtJMFzlpplr", "TWjTnTTrjVsVvvTnTs")
SAME_ITEM = "r"


class TestRucksackReorganization:
    def test_split_string(self):
        rucksacks = split_in_two(RUCKSACK)
        assert rucksacks == RUCKSACKS

    def test_get_same_item(self):
        same_item = get_same_item(RUCKSACKS)
        assert same_item == SAME_ITEM

    def test_get_rucksack_priorioties(self):
        rucksack_score = get_rucksack_priorities(SAME_ITEM)
        assert rucksack_score == 18
