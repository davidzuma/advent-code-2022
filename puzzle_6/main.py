from typing import List, Tuple

with open("puzzle_6/input.txt", "r") as file:
    datastream = file.read()

a = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
b = "bvwbjplbgvbhsrlpgdmjqwftvncz"
c = "nppdvjthqldpwncqszvftbrmjlhg"
d = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
e = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"


def find_first_no_repeated_string(string: str, long) -> int:
    input_string = string
    no_repeated_string = ""
    repeated_string_position = 0
    while len(no_repeated_string) != long:
        if string[repeated_string_position] in no_repeated_string:
            repeated_string_position = no_repeated_string.find(
                string[repeated_string_position]
            )

            string = string[repeated_string_position + 1 :]
            no_repeated_string = ""
            repeated_string_position = 0

        else:
            no_repeated_string += string[repeated_string_position]
            repeated_string_position += 1
    return input_string.find(no_repeated_string)


print("--Part 1---")
print(find_first_no_repeated_string(datastream, 4) + 4)

print("--Part 2---")
print(find_first_no_repeated_string(datastream, 14) + 14)
