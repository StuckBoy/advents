directions = "^>v<"
santa_coords = [0,0]
robo_santa_coords = [0,0]
santa_coord_list = ["0,0"]
robo_santa_coord_list = ["0,0"]

if __name__ == '__main__':
    data = open('input.txt', 'r')
    inputs = data.read().strip('\n')
    santa = inputs[0:][::2]
    robo_santa = inputs[1:][::2]

    for direction in santa:
        if direction == ">":
            santa_coords[0] += 1
        if direction == "<":
            santa_coords[0] -= 1
        if direction == "^":
            santa_coords[1] += 1
        if direction == "v":
            santa_coords[1] -= 1
        santa_coord_list.append(str(santa_coords[0])+","+str(santa_coords[1]))
    santa_count = len(set(santa_coord_list))

    for direction in robo_santa:
        if direction == ">":
            robo_santa_coords[0] += 1
        if direction == "<":
            robo_santa_coords[0] -= 1
        if direction == "^":
            robo_santa_coords[1] += 1
        if direction == "v":
            robo_santa_coords[1] -= 1
        robo_santa_coord_list.append(str(robo_santa_coords[0])+","+str(robo_santa_coords[1]))
    robo_count = len(set(robo_santa_coord_list))
    merged_count = len(set(santa_coord_list + robo_santa_coord_list))
    print(merged_count)