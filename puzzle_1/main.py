with open("puzzle_1/input.txt", "r") as file:
    elves_data_text = file.read()
elves_calories_split = elves_data_text.split("\n\n")
elves_num = len(elves_calories_split)
elves_calories = sorted(
    (sum(map(int, elf.split("\n"))) for elf in elves_calories_split)
)
# --- Part One ---
print(elves_calories[-1:][0])
# --- Part Two ---
print(sum(elves_calories[-3:]))
