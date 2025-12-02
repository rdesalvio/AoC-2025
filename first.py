# assumes format {direction}{number}
def get_location(current: int, combination: str):
    direction = combination[0]
    movement = int(combination[1:])

    laps = movement // 100
    movement = movement % 100
    started_at_zero = current == 0
    if direction == 'L':
        current -= movement
    else:
        current += movement
    
    if current < 0:
        return 100 + current, laps + 1 if not started_at_zero else laps
    elif current > 99:
        return abs(100 - current), laps + 1 if current != 100 and not started_at_zero else laps
    return current, laps

def run():
    # start at position 50
    pos = 50
    counter = 0
    with open("inputs/1.txt", "r") as file:
        for line in file:
            pos, laps = get_location(pos, line.strip())
            counter += laps
            if pos == 0:
                counter += 1
    
    return counter

if __name__ == "__main__":
    print(run())