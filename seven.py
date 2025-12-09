
def count_splits(carrots, starting_index):
    current_beams = []
    split_counter = 0
    has_used_starting_index = False
    for row in carrots:
        for char_idx in row:
            if not has_used_starting_index and char_idx == starting_index:
                split_counter += 1
                current_beams = [idx for idx in current_beams if idx != char_idx]
                current_beams.append(char_idx+1)
                current_beams.append(char_idx-1)
                has_used_starting_index = True
            elif char_idx in current_beams:
                split_counter += 1
                current_beams = [idx for idx in current_beams if idx != char_idx]
                current_beams.append(char_idx+1)
                current_beams.append(char_idx-1)
    return split_counter


def timeline(row, col, grid, timelines):
    if row == len(grid):
        return timelines
    if grid[row][col] == '^':
        print("incrementing")
        timeline(row+1, col-1, grid, timelines+1)
        timeline(row+1, col+1, grid, timelines+1)
    if grid[row][col] == '.' or grid[row][col] == 'S':
        timeline(row+1, col, grid, timelines)
    return timelines



if __name__ == "__main__":
    grid = []
    starting_idx = -1
    with open("inputs/7.txt", "r") as file:
        for line in file:
            row = []
            for idx, char in enumerate(line.strip()):
                if starting_idx == -1 and char == 'S':
                    starting_idx = idx
                row.append(char)
            grid.append(row)
    #print(count_splits(carrots, starting_idx))
    print(grid)
    print(starting_idx)
    print(timeline(0, starting_idx, grid, 0))
        
