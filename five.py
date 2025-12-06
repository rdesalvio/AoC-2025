def is_spoiled(ranges, id):
    for range in ranges:
        if id >= range[0] and id <= range[1]:
            return True
    return False

def count_fresh_ids(ranges):
    i = 0
    while i < len(ranges):
        current = ranges[i]
        updated = -1
        for idx, inner_range in enumerate(ranges):
            if i == idx:
                continue
            if current[0] <= inner_range[0] and current[1] >= inner_range[0]:
                ranges[i] = (current[0], max(inner_range[1], current[1]))
                updated = idx
                break
            if current[1] <= inner_range[1] and current[0] >= inner_range[0]:
                ranges[i] = (min(inner_range[0], current[0]), inner_range[1])
                updated = idx
                break
        if updated != -1:
            del ranges[updated]
            i = 0
            continue
        i += 1

    sum = 0
    for inner_range in ranges:
        sum += (inner_range[1]-inner_range[0])+1
    print(sum)

if __name__ == "__main__":
    ranges = []
    count = 0
    with open("inputs/5.txt", "r") as file:
        for line in file:
            input = line.strip()
            if "-" in input:
                numerical_range = input.split('-')
                ranges.append((int(numerical_range[0]), int(numerical_range[1])))
            if '-' not in input and input != '':
                if is_spoiled(ranges, int(input)):
                    count += 1
    count_fresh_ids(ranges)
            