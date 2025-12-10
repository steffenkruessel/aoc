# calculate the area two tiles are covering
def rectangle_area(tile_a, tile_b):
    return (
        (abs(int(tile_a[0])-int(tile_b[0]))+1) *
        (abs(int(tile_a[1])-int(tile_b[1]))+1)
    )

# check if a given tile (c) is part of a given rectangle (a, b)
def is_corner(tile_a, tile_b, tile_c):
    if (tile_c[0] == tile_a[0] and tile_c[1] == tile_b[1] or
        tile_c[0] == tile_b[0] and tile_c[1] == tile_a[1]):
        return True
    else:
        return False

# checks if a given rectangle (a, b) is contained in the area of all tiles given
def is_contained_in_tiles(tiles, tile_a, tile_b):
    tile_c = [tile_a[0], tile_b[1]]
    tile_d = [tile_b[0], tile_a[1]]
    print("Area:", tile_a, tile_b, tile_c, tile_d)

    min_x = min(int(tile_a[0]), int(tile_b[0]))
    max_x = max(int(tile_a[0]), int(tile_b[0]))
    min_y = min(int(tile_a[1]), int(tile_b[1]))
    max_y = max(int(tile_a[1]), int(tile_b[1]))

    top_left_in_tiles, bottom_left_in_tiles, top_right_in_tiles, bottom_right_in_tiles = False, False, False, False
    for tile in tiles:
        tile_pos_x = int(tile[0])
        tile_pos_y = int(tile[1])

        if not top_left_in_tiles:
            if tile_pos_x <= min_x and tile_pos_y <= min_y: top_left_in_tiles = True
        if not bottom_left_in_tiles:
            if tile_pos_x >= max_x and tile_pos_y <= min_y: bottom_left_in_tiles = True
        if not top_right_in_tiles:
            if tile_pos_x <= min_x and tile_pos_y >= max_y: top_right_in_tiles = True
        if not bottom_right_in_tiles:
            if tile_pos_x >= max_x and tile_pos_y >= max_y: bottom_right_in_tiles = True

    if top_left_in_tiles and bottom_left_in_tiles and top_right_in_tiles and bottom_right_in_tiles:
        return True
    else:
        return False

def is_contained_in_area(floor, tile_a, tile_b):
    for row_index in range(min(int(tile_a[1]), int(tile_b[1])), max(int(tile_a[1]), int(tile_b[1]))):
        for column_index in range(min(int(tile_a[0]), int(tile_b[0])), max(int(tile_a[0]), int(tile_b[0]))):
            #print(floor[row_index][column_index])
            if floor[row_index][column_index] == ".":
                return False
    return True

tiles = []
with open("input.txt", "r") as file:
    for line in file:
        tiles.append(line.strip("\n\r").split(","))
print("Tiles:", tiles)

tiles_int = []
for tile in tiles:
    tiles_int.append([int(tile[0]), int(tile[1])])
print("Tiles (int):", tiles_int)

tiles_sorted_x = sorted(tiles_int, key=lambda x: x[1])
print("Tiles (x):", tiles_sorted_x)
tiles_sorted_y = sorted(tiles_int, key=lambda x: x[0])
print("Tiles (y):", tiles_sorted_y)

tile_x_draw = []
for row_index in range(len(tiles_sorted_x)):
    x_coordinate = tiles_sorted_x[row_index][1]
    if not any(x_coordinate in coordinate for coordinate in tile_x_draw):
        tile_x_draw.append([x_coordinate, [tiles_sorted_x[row_index][0]]])
    else:
        for i in range(len(tile_x_draw)):
            if tile_x_draw[i][0] == x_coordinate:
                tile_x_draw[i][1].append(tiles_sorted_x[row_index][0])
for x_draw_item in tile_x_draw: x_draw_item[1].sort()
print(tile_x_draw)

tile_y_draw = []
for row_index in range(len(tiles_sorted_y)):
    y_coordinate = tiles_sorted_y[row_index][0]
    if not any(y_coordinate in coordinate for coordinate in tile_y_draw):
        tile_y_draw.append([y_coordinate, [tiles_sorted_y[row_index][1]]])
    else:
        for i in range(len(tile_y_draw)):
            if tile_y_draw[i][0] == y_coordinate:
                tile_y_draw[i][1].append(tiles_sorted_y[row_index][1])
for y_draw_item in tile_y_draw: y_draw_item[1].sort()
print(tile_y_draw)

print("-- Tiles --")
floor = []
for row_index in range(tiles_sorted_x[-1][1] + 2):
    row = ""
    already_drawn = False

    columns_to_draw_red = []
    columns_to_draw_green = []
    for x in tile_x_draw:
        if x[0] == row_index:
            # draw red tiles
            columns_to_draw_red = x[1]
            for column_tmp_index in range(x[1][0]+1, x[1][-1]):
                # draw green row wide between red tiles
                columns_to_draw_green.append(column_tmp_index)

    for column_index in range(tiles_sorted_y[-1][0] + 3):
        for y in tile_y_draw:
            if y[0] == column_index:
                for row_tmp_index in range(y[1][0]+1, y[1][-1]):
                    if row_tmp_index == row_index:
                        # draw green column wide between red tiles
                        columns_to_draw_green.append(column_index)

    #print("columns", columns_to_draw_green)
    if len(columns_to_draw_green) > 0:
        for column_index in range(min(columns_to_draw_green) + 1, max(columns_to_draw_green)):
            columns_to_draw_green.append(column_index)

    for column_index in range(tiles_sorted_y[-1][0] + 3):
        if column_index in columns_to_draw_red:
            row += "#"
        elif column_index in columns_to_draw_green:
            row += "X"
        else: row += "."
    #print(row)

    floor.append(row)

tile_areas = []
for tile_a_index in range(0, len(tiles)):
    for tile_b_index in range(tile_a_index+1, len(tiles)):
        area_tuple = []
        area_tuple.append(rectangle_area(tiles[tile_a_index], tiles[tile_b_index]))
        area_tuple.append([tile_a_index, tile_b_index])
        tile_areas.append(area_tuple)
print("Areas:", tile_areas)

valid_tile_areas = []
for area_tuple in sorted(tile_areas, key=lambda x: x[0], reverse=True):
    for tile_index in range(len(tiles)):
        if tile_index != area_tuple[1][0] and tile_index != area_tuple[1][1]:
            if is_contained_in_area(floor, tiles[area_tuple[1][0]], tiles[area_tuple[1][1]]):
                valid_tile_areas.append(area_tuple)
'''
            if is_corner(tiles[area_tuple[1][0]], tiles[area_tuple[1][1]], tiles[tile_index]):
                print("Analyzed Tile", tile_index, "for Area", area_tuple)
                print("Tile", tiles[tile_index], "is part of rectangle between", tiles[area_tuple[1][0]], "and", tiles[area_tuple[1][1]])
                if is_contained_in_tiles(tiles, tiles[area_tuple[1][0]], tiles[area_tuple[1][1]]):
                    print("Area", tiles[area_tuple[1][0]], tiles[area_tuple[1][1]], "seems to be fine.")
                    valid_tile_areas.append(area_tuple)
'''
max_area = valid_tile_areas[0][0]
print("Solution:", max_area)
