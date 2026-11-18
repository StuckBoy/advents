if __name__ == '__main__':
    data = open("input.txt", "r")
    floor = 0
    for char in data.read():
        if char == '(':
            floor += 1
        elif char == ')':
            floor -= 1
    print(floor)