if __name__ == '__main__':
    input = open("input.txt", "r")
    floor = 0
    count = 0
    for char in input.read():
        count += 1
        if char == '(':
            floor += 1
        elif char == ')':
            floor -= 1
        if floor < 0:
            break
    print(count)