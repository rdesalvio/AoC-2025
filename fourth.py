def paper_counter(grid, point):
    first = point[0]+1, point[1]
    second = point[0]+1, point[1]+1
    third = point[0]+1, point[1]-1
    fourth = point[0]-1, point[1]+1
    fifth = point[0]-1, point[1]-1
    sixth = point[0]-1, point[1]
    seventh = point[0], point[1]-1
    eigth = point[0], point[1]+1
    
    spaces = [first, second, third, fourth, fifth, sixth, seventh, eigth]
    paper_counter = 0
    for space in spaces:
        if space[0] < 0 or space[1] < 0:
            continue
        try:
            if grid[space[0]][space[1]] == "@":
                paper_counter += 1
        except IndexError:
            continue
    return paper_counter

def part_one(grid):
    counter = 0
    snapshot = 1
    while snapshot != counter:
        snapshot = counter
        for i, row in enumerate(grid):
            for j, _ in enumerate(row):
                if grid[i][j] == "@":
                    if paper_counter(grid, (i,j)) < 4:
                        grid[i][j] = '.'
                        counter += 1
    print(counter)

if __name__ == "__main__":
    with open("inputs/4.txt") as file:
        grid = []
        for line in file:
            row = []
            for char in line.strip():
                row.append(char)
            grid.append(row)
        part_one(grid)