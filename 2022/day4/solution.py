def read_day4_input(input_file_name) -> list:
    f = open(input_file_name, "r")
    input_list = f.read().splitlines()

    return [i.split(",") for i in input_list]


def seperate_sections(pair: list) -> list:
    return [list(map(int, i.split("-"))) for i in pair]


def check_if_contains_all(pair: list) -> bool:
    first = pair[0]
    second = pair[1]

    if (first[0] <= second[0] and first[1] >= second[1]) or (
        first[0] >= second[0] and first[1] <= second[1]
    ):
        return True
    return False


def check_if_contains_any(pair: list) -> bool:
    first = range(pair[0][0], pair[0][1] + 1)
    second = range(pair[1][0], pair[1][1] + 1)

    if len(set(first).intersection(set(second))) >= 1:
        return True
    return False


# PART 1
input_pairs = read_day4_input("input.txt")
input_pairs = list(map(seperate_sections, input_pairs))

compared_pairs_all = list(map(check_if_contains_all, input_pairs))
print("# of contained pairs: ", sum(compared_pairs_all))

# PART 2
compared_pairs_any = list(map(check_if_contains_any, input_pairs))
print("# of contained pairs: ", sum(compared_pairs_any))
