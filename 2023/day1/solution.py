import re


def read_input(input_file_name: str) -> list[str]:
    f = open(input_file_name, "r")
    input_string = f.read()

    return input_string.splitlines()


def analyze_row(row: str) -> int:
    numeric_only: str = re.sub(r"[^0-9.]", "", row)
    # Minimum string lenght is 2
    if len(numeric_only) >= 2:
        return int(numeric_only[0] + numeric_only[-1])

    return int(numeric_only + numeric_only)


def analyze_row_part_2(row: str):
    pattern = [
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]

    converted_str: str = row
    for index in range(len(row) + 1):
        included_index = [
            converted_str[0:index].find(word) > -1 for word in pattern
        ]

        if any(included_index):
            found_num = included_index.index(True)

            converted_str = converted_str.replace(
                pattern[found_num],
                str(found_num) + pattern[found_num][1:],
            )
    return analyze_row(converted_str)


def main():
    input_rows: list[str] = read_input("input.txt")
    values_part_1: list[int] = [analyze_row(row=row) for row in input_rows]
    solution_part_1: int = sum(values_part_1)

    values_part_2: list[int] = [
        analyze_row_part_2(row=row) for row in input_rows
    ]
    solution_part_2: int = sum(values_part_2)

    print("Solution PART 1: ", solution_part_1)
    print("Solution PART 2: ", solution_part_2)


if __name__ == "__main__":
    main()
