# part 1
def is_repeating(num: str) -> bool:
    if len(num) % 2 != 0:
        return False

    midpoint = len(num) // 2
    return num[0:midpoint] == num[midpoint:]

# part 2
def is_invalid_product_id(product_id: str) -> bool:
    for divisor in range(1, len(product_id)):
        # repeating strings have to be evenly divisible by total length
        if len(product_id) % divisor != 0:
            continue
        
        repeating_string = product_id[0:divisor]
        trail, head = 0, divisor
        while head <= len(product_id):
            if product_id[trail:head] != repeating_string:
                break
            trail += divisor
            head += divisor

        # we successfully matched the entire string
        if head-divisor == len(product_id):
            return True

    return False
        
if __name__ == "__main__":
    with open("inputs/2.txt", "r") as file:
        sum = 0
        for num_range in file.readline().split(","):
            numbers = num_range.split('-')
            low, high = numbers[0], numbers[1]
            for i in range(int(low), int(high)+1):
                if is_invalid_product_id(str(i)):
                    sum += i
        print(sum)