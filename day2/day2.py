def read_day2_input(input_file_name):
    f = open(input_file_name, "r")
    input_list = f.read().splitlines()

    return [tuple(i.split(" ")) for i in input_list]


def calculate_winner(round: tuple):
    selection_score = {"X": 1, "Y": 2, "Z": 3}

    score = selection_score[round[1]]
    if (
        (round[1] == "X" and round[0] == "C")
        or (round[1] == "Y" and round[0] == "A")
        or (round[1] == "Z" and round[0] == "B")
    ):
        score += 6
    elif (
        (round[1] == "X" and round[0] == "A")
        or (round[1] == "Y" and round[0] == "B")
        or (round[1] == "Z" and round[0] == "C")
    ):
        score += 3
    return score


def calculate_winner_new(round: tuple):
    selection_score = {"rock": 1, "paper": 2, "scissors": 3}

    score = 0
    if round[1] == "X":
        if round[0] == "A":
            score += selection_score["scissors"]
        elif round[0] == "B":
            score += selection_score["rock"]
        elif round[0] == "C":
            score += selection_score["paper"]
    elif round[1] == "Y":
        score += 3
        if round[0] == "A":
            score += selection_score["rock"]
        elif round[0] == "B":
            score += selection_score["paper"]
        elif round[0] == "C":
            score += selection_score["scissors"]
    elif round[1] == "Z":
        score += 6
        if round[0] == "A":
            score += selection_score["paper"]
        elif round[0] == "B":
            score += selection_score["scissors"]
        elif round[0] == "C":
            score += selection_score["rock"]

    return score


input_strategy = read_day2_input("input.txt")
all_scores_part1 = list(map(calculate_winner, input_strategy))
all_scores_part2 = list(map(calculate_winner_new, input_strategy))

print("Total Score Part 1: ", sum(all_scores_part1))
print("Total Score Part 2: ", sum(all_scores_part2))
