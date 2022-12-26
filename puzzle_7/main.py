import re


with open("puzzle_7/input.txt") as file:
    command_lines = file.read()

all_numbers = re.findall("[0-9]+", command_lines)

f = lambda x: x.split("\n")[:-1]
command_list = list(map(f, command_lines.split("$ ")))[1:]


def flatten(l):
    return [item for sublist in l for item in sublist]


def is_digits_list(xs: list):
    are_digits = list(map(lambda x: x.isdigit(), xs))
    non_digits_positions = [xs[id] for id, b in enumerate(are_digits) if not b]
    return all(are_digits), non_digits_positions


class CommandLine:
    def __init__(self):
        self.current_dir = ""
        self.directory_summary = dict()

    def _move_to_dir(self, root):
        root = "" if root == "/" else root

        if root == "..":
            self.current_dir = "/".join(self.current_dir.split("/")[:-1])
        else:
            self.current_dir += f"/{root}"
        self.current_dir = self.current_dir.replace("//", "/")

    def _save_to_directory_summary(self, directories_and_files):
        self.directory_summary[self.current_dir] = [
            d.split(" ")[0] for d in directories_and_files
        ]

    def apply_command(self, command):
        command_type, *directories = command
        dir = "/" if self.current_dir == "/" else f"{self.current_dir}/"
        directories_parsed = list(map(lambda x: x.replace("dir ", dir), directories))
        cd_or_ls, *root = command_type.split(" ")
        if cd_or_ls == "cd":
            self._move_to_dir(root[0])
        else:
            self._save_to_directory_summary(directories_parsed)

    def get_directories_size(self):
        directories_size = dict()

        for k, v in self.directory_summary.items():
            are_all_digits, non_digits = is_digits_list(v)
            v_with_size = v
            while not are_all_digits:
                v_with_size = flatten(
                    [self.directory_summary[i] for i in v if i in non_digits]
                ) + [i for i in v_with_size if i not in non_digits]
                are_all_digits, non_digits = is_digits_list(v_with_size)
            directories_size[k] = sum(map(int, v_with_size))

        return directories_size


command_obj = CommandLine()

for command in command_list:
    command_obj.apply_command(command)

directories_size = command_obj.get_directories_size()
directories_to_rm = {k: v for k, v in directories_size.items() if v <= 100000}
system_used_space = directories_size["/"]
system_free_space = 70000000 - sum(map(int, all_numbers))
print(
    sorted([i for i in directories_size.values() if i >= 30000000 - system_free_space])
)


# Solution part 1
print(sum(directories_to_rm.values()))
