def calc_ribbon(length, width, height):
    sizes = [length, width, height]
    sizes.sort()
    side_one = sizes[0]+sizes[0]
    side_two = sizes[1]+sizes[1]
    return side_one + side_two

def calc_bow(length, width, height):
    return length * width * height

if __name__ == '__main__':
    data = open('input.txt', 'r')
    dimensions = data.readlines()
    total = 0
    for dimension in dimensions:
        values = dimension.strip('\n').split('x')
        ribbon = calc_ribbon(int(values[0]), int(values[1]), int(values[2]))
        bow = calc_bow(int(values[0]), int(values[1]), int(values[2]))
        total += ribbon + bow
    print(total)