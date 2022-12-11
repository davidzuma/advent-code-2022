from typing import Tuple

rock_paper_scissors_file = open("puzzle_2/input.txt", "r")
rock_paper_scissors: str = rock_paper_scissors_file.read()
rock_paper_scissors_games: list = rock_paper_scissors.split("\n")


MOVE_MAP = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}
RESULT_MAP = {"X": 0, "Y": 3, "Z": 6}


def get_strategy_score(rock_paper_scissors_games: list[str]) -> Tuple[int, int]:
    games_score = map(get_game_score, rock_paper_scissors_games)
    games_score_2 = map(get_game_score_2, rock_paper_scissors_games)

    return sum(games_score), sum(games_score_2)


# part 1 score
def get_game_score(rock_paper_scissors_game: str) -> int:
    opponent_move, my_move = get_move(rock_paper_scissors_game)
    move_result = opponent_move - my_move
    game_score = 0
    # move = 0 when it is a draw
    if move_result == 0:
        game_score = 3
    # move = -1 or move = 2 means my_move is a winner move
    elif move_result == -1 or move_result == 2:
        game_score = 6
    # else my_move is a losser move
    return game_score + my_move


# part 2 score
def get_game_score_2(rock_paper_scissors_game: str) -> int:
    opponent_move, game_score = get_move(rock_paper_scissors_game, is_result=True)
    # game_score = 3 means is a draw then my move = opponent move
    if game_score == 3:
        my_move = opponent_move
    # game_score = 6 means my move is a winner move
    elif game_score == 6:
        if opponent_move == 3:
            my_move = opponent_move - 2
        else:
            my_move = opponent_move + 1
    # else game_score = 0 means my move is a loser move
    else:
        if opponent_move == 1:
            my_move = opponent_move + 2
        else:
            my_move = opponent_move - 1
    return game_score + my_move


def get_move(rock_paper_scissors_game: str, is_result: bool = False) -> Tuple[str, str]:
    opponent_move, my_move_or_result = rock_paper_scissors_game.split(" ")

    return (
        MOVE_MAP[opponent_move],
        RESULT_MAP[my_move_or_result] if is_result else MOVE_MAP[my_move_or_result],
    )


if __name__ == "__main__":

    print(get_strategy_score(rock_paper_scissors_games))
