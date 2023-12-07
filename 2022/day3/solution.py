import string


def read_day3_input(input_file_name) -> list:
    f = open(input_file_name, "r")
    input_list = f.read().splitlines()

    return input_list


def calculate_priority(content: tuple) -> int:
    alphabet = {
        value: index + 1 for index, value in enumerate(string.ascii_letters)
    }

    # find common letter between contents
    common_letter = list(
        set(content[0]).intersection(
            *[set(content[i]) for i in range(1, len(content))]
        )
    )[0]
    return alphabet[common_letter]


# PART 1
input_contents = [
    (i[: (len(i) // 2)], i[(len(i) // 2) :])
    for i in read_day3_input("input.txt")
]
priorities = list(map(calculate_priority, input_contents))

print("Total Priority: ", sum(priorities))

# PART 2
input_groups_contents = read_day3_input("input.txt")
input_groups_contents = [
    (
        input_groups_contents[i],
        input_groups_contents[i + 1],
        input_groups_contents[i + 2],
    )
    for i in range(0, len(input_groups_contents), 3)
]
groups_priorites = list(map(calculate_priority, input_groups_contents))

print("Total Priority Groups: ", sum(groups_priorites))
