import re


def read_input(input_file_name: str) -> dict:
    f = open(input_file_name, "r")
    input_list = f.read().splitlines()

    colors = ("red", "blue", "green")
    input_games: dict = {}
    for row in input_list:
        [game_id, game_info] = row.split(":")

        game_info = game_info.split(";")

        subsets: list = []
        maximum: dict = {"red": 0, "blue": 0, "green": 0}
        for i in range(len(game_info)):
            subsets.append({})
            round = game_info[i].split(",")

            for j in round:
                # RED
                num = int(re.sub(r"[^0-9.]", "", j))

                if colors[0] in j:
                    subsets[i][colors[0]] = num
                    maximum[colors[0]] = max(maximum[colors[0]], num)
                # BLUE
                if colors[1] in j:
                    subsets[i][colors[1]] = num
                    maximum[colors[1]] = max(maximum[colors[1]], num)

                # GREEN
                if colors[2] in j:
                    subsets[i][colors[2]] = num
                    maximum[colors[2]] = max(maximum[colors[2]], num)

        input_games[re.sub(r"[^0-9.]", "", game_id)] = {
            "maximum": maximum,
            "subsets": subsets,
        }

    return input_games


def check_is_possible(game, condition: dict) -> bool:
    for color, cond in condition.items():
        if game["maximum"][color] > cond:
            return False

    return True


def power_minimum_set(game) -> int:
    power: int = 1

    for color in ("red", "blue", "green"):
        power *= game["maximum"][color]

    return power


def main():
    input_games: dict[str, dict] = read_input("input.txt")

    possible_games: list[int] = [
        int(id)
        if check_is_possible(
            game=game, condition={"red": 12, "green": 13, "blue": 14}
        )
        else 0
        for id, game in input_games.items()
    ]
    sum_possible_games: int = sum(possible_games)
    print("Solution PART 1: ", sum_possible_games)

    power_minumum_sets: list[int] = [
        int(power_minimum_set(game)) for game in input_games.values()
    ]
    sum_power_minumum_sets: int = sum(power_minumum_sets)
    print("Solution PART 2: ", sum_power_minumum_sets)


if __name__ == "__main__":
    main()
