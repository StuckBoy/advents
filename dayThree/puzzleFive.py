directions = "^>v<"
coords = [0,0]
coord_list = ["0,0"]

if __name__ == '__main__':
    data = open('input.txt', 'r')
    inputs = data.read()
    for direction in inputs.strip('\n'):
        if direction == ">":
            coords[0] += 1
        if direction == "<":
            coords[0] -= 1
        if direction == "^":
            coords[1] += 1
        if direction == "v":
            coords[1] -= 1
        coord_list.append(str(coords[0])+","+str(coords[1]))
    print(len(set(coord_list)))