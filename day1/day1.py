import re


def read_day1_input(input_file_name):
    f = open(input_file_name, "r")
    input_string = f.read()
    seperate_elves = re.split(r"\n{2}", input_string.strip())
    seperate_calories = [
        list(map(int, re.split(r"\n", i.strip()))) for i in seperate_elves
    ]

    return seperate_calories


def get_maximum_n(calories, n):
    totals = list(map(sum, calories))
    sorted_totals = sorted(totals, reverse=True)

    return sum(sorted_totals[:n])


input_calories = read_day1_input("input.txt")
print("Maximum calories: ", get_maximum_n(calories=input_calories, n=1))
print("Maximum 3 calories: ", get_maximum_n(calories=input_calories, n=3))
