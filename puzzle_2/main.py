rock_paper_scissors_file = open("puzzle_2/input.txt", "r")
rock_paper_scissors: str = rock_paper_scissors_file.read()
rock_paper_scissors_games: list = rock_paper_scissors.split("\n")


MOVE_MAP = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}


def get_strategy_score(rock_paper_scissors_games: list) -> int:
    games_score = map(get_game_score, rock_paper_scissors_games)
    return sum(games_score)


def get_game_score(rock_paper_scissors_games: str):
    opponent_move = rock_paper_scissors_games.split(" ")[0]
    my_move = rock_paper_scissors_games.split(" ")[1]
    game_score = MOVE_MAP[my_move]
    move = MOVE_MAP[opponent_move] - MOVE_MAP[my_move]
    if move == 0:
        game_score += 3
    elif move % 3 == -1:
        game_score += 6
    return game_score


if __name__ == "__main__":
    print(get_strategy_score(rock_paper_scissors_games))
