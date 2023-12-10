def read_input(input_file_name):
    f = open(input_file_name, "r")
    input_list = f.read().splitlines()
    return input_list


def control_hold(hold_arr: list) -> bool:
    # print("CONTROL HOLD")
    # breakpoint()
    if all(
        [
            i == "."
            for i in hold_arr[0]
            + hold_arr[1][0]
            + hold_arr[1][-1]
            + hold_arr[2]
        ]
    ):
        return False
    return True


def analyze_row(row: str, above: str, below: str, index: int) -> list[int]:
    hold_arr = [above[0], row[0], below[0]]
    hold_num = ""

    part_nums: list[int] = []
    for i in range(1, len(row) - 1):
        if row[i] != ".":
            if row[i].isnumeric():
                hold_arr[0] += above[i]
                hold_arr[1] += row[i]
                hold_arr[2] += below[i]

                hold_num += row[i]
            else:
                hold_arr = [above[i], row[i], below[i]]
                hold_num = ""
                continue

            if row[i + 1].isnumeric():
                continue
            else:
                controlled_hold = control_hold(
                    [
                        hold_arr[0] + above[i + 1],
                        hold_arr[1] + row[i + 1],
                        hold_arr[2] + below[i + 1],
                    ]
                )

                if controlled_hold:
                    part_nums.append(int(hold_num))

        hold_arr = [above[i], row[i], below[i]]
        hold_num = ""

    return part_nums


def main():
    input_schematic: list[str] = read_input("input.txt")
    new = (
        ["." * len(input_schematic[0])]
        + input_schematic
        + ["." * len(input_schematic[0])]
    )

    row_part_nums = []
    for i in range(1, len(new) - 1):
        rowww = analyze_row(
            row="." + new[i] + ".",
            above="." + new[i - 1] + ".",
            below="." + new[i + 1] + ".",
            index=i,
        )

        row_part_nums += rowww

    print(sum(row_part_nums))


if __name__ == "__main__":
    main()
