def surface_area(length, width, height):
    side_one =  length * width
    side_two =  width * height
    side_three = height * length
    smallest = min(side_one, side_two, side_three)
    return (2 * side_one) + (2* side_two) + (2 * side_three) + smallest

if __name__ == '__main__':
    data = open('input.txt', 'r')
    dimensions = data.readlines()
    total = 0
    for dimension in dimensions:
        values = dimension.strip('\n').split('x')
        total += surface_area(int(values[0]), int(values[1]), int(values[2]))
    print(total)