def multiply(numbers):
    answer = 1
    for num in numbers:
        answer *= num
    return answer


def add(numbers):
    answer = 0
    for num in numbers:
        answer += num
    return answer


def calculate_answers(grid, operation_row):
    column_ranges = []
    operations = []
    for idx, char in enumerate(operation_row):
        if char == '*' or char == '+':
            column_ranges.append(idx)
            operations.append(char)

    idx = 0
    totals = []
    while idx < len(column_ranges):
        if idx+1 >= len(column_ranges):
            current_range = (column_ranges[idx], len(grid[0]))
        else:
            current_range = (column_ranges[idx], column_ranges[idx+1])

        if operations[idx] == '+':
            totals.append(add(parse_cephalopod_math(grid, current_range)))
        elif operations[idx] == '*':
            totals.append(multiply(parse_cephalopod_math(grid, current_range)))
        else:
            raise("unsupported operations found")

        idx += 1

    return totals


def parse_cephalopod_math(grid, column_range):
    beginning, end = column_range[0], column_range[1]-1
    numbers = []
    while end >= beginning:
        new_number = ''
        for row in grid:
            new_number += row[end]
        new_number = new_number.strip()
        if new_number == '':
            end -= 1
            continue
        numbers.append(int(new_number))
        end -= 1
    return numbers
    

def update_grid(grid, row, line):
    grid.append([])
    for char in line:
        grid[row].append(char)
    return grid


if __name__ == "__main__":
    with open("inputs/6.txt", "r") as file:
        totals = []
        grid = []
        for row, line in enumerate(file):
            inputs = line.strip('\n')
            if inputs[0] == '+' or inputs[0] == '*':
                totals = calculate_answers(grid, inputs)
                break
            update_grid(grid, row, inputs)

        print(sum(totals))