from typing import List, Tuple
import re

with open("puzzle_5/input.txt", "r") as file:
    board_and_moves = file.read()
board, moves = board_and_moves.split("\n\n")
board_parsed = (
    board.replace("[", "").replace("]", "").replace("  ", " ").split("\n")[:-1]
)
board_len = len(board_parsed)
board_stacks = [[j[i * 2] for j in board_parsed if j[i * 2] != " "] for i in range(9)]

moves: list = moves.split("\n")
find_numbers = lambda s: [int(num) for num in re.findall(r"[0-9]+", s)]
moves_parsed = list(map(find_numbers, moves))


class CratesStack:
    def __init__(self, board):
        self.board = board

    def move_crates(self, number_of_crates, stack_origin, stack_destination):
        crates = self.board[stack_origin - 1][:number_of_crates][::-1]
        self.board[stack_origin - 1] = self.board[stack_origin - 1][number_of_crates:]
        self.board[stack_destination - 1] = crates + self.board[stack_destination - 1]

    def move_crates_reverse(self, number_of_crates, stack_origin, stack_destination):
        crates = self.board[stack_origin - 1][:number_of_crates]
        self.board[stack_origin - 1] = self.board[stack_origin - 1][number_of_crates:]
        self.board[stack_destination - 1] = crates + self.board[stack_destination - 1]

    def get_top_of_each_stack(self):
        return "".join([stack[0] for stack in self.board if stack != []])


crates_stack_obj = CratesStack(board_stacks)

for move in moves_parsed:
    crates_stack_obj.move_crates_reverse(*move)
print(crates_stack_obj.get_top_of_each_stack())
