
def rectangle_area(tile_a, tile_b):
    return (
        (abs(int(tile_a[0])-int(tile_b[0]))+1) *
        (abs(int(tile_a[1])-int(tile_b[1]))+1)
    )

tiles = []
with open("input.txt", "r") as file:
    for line in file:
        tiles.append(line.strip("\n\r").split(","))
print("Tiles:", tiles)

tile_areas = []
for tile_a_index in range(0, len(tiles)):
    for tile_b_index in range(tile_a_index+1, len(tiles)):
        area_tuple = []
        area_tuple.append(rectangle_area(tiles[tile_a_index], tiles[tile_b_index]))
        area_tuple.append([tile_a_index, tile_b_index])
        tile_areas.append(area_tuple)
print("Areas:", tile_areas)

max_area = 0
for area_tuple in sorted(tile_areas, key=lambda x: x[0], reverse=True):
    print("Max Area:", area_tuple)
    max_area = area_tuple[0]
    break

print("Solution:", max_area)