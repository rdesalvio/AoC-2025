
def find_joltage(bank: str) -> int:
    first, second = int(bank[0]), 0
    idx = 1
    while idx < len(bank):
        cur = int(bank[idx])
        if cur > first and idx != len(bank)-1:
            first = cur
            second = int(bank[idx+1])
        elif cur > second:
            second = cur
        idx += 1
    return int(str(first) + str(second))


def find_highest_leftmost(group):
    highest = -1
    finish = 0
    for idx, num in enumerate(group):
        if int(num) > highest:
            highest = int(num)
            finish = idx

    return finish, highest


def find_overload_joltage(bank: str):
    selected_numbers = []
    leftmost_idx = 0
    while len(selected_numbers) != 12:
        if len(selected_numbers) == 11:
            selection_group = bank
        else:
            selection_group = bank[:-(12-len(selected_numbers)-1)]
        leftmost_idx, highest = find_highest_leftmost(selection_group)
        selected_numbers.append(str(highest))
        bank = bank[leftmost_idx+1:]
    return int("".join(selected_numbers))

if __name__ == "__main__":
    with open("inputs/3.txt") as file:
        total_joltage = 0
        for line in file:
            joltage = find_overload_joltage(line.strip()) 
            total_joltage += joltage
    
        print(total_joltage)