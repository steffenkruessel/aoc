
from shapely.geometry import Polygon
import matplotlib.pyplot as plt
import geopandas as gpd

# calculate the area two tiles are covering
def rectangle_area(tile_a, tile_b):
    '''
    area_self = ((abs(int(tile_a[0])-int(tile_b[0]))+1) *
        (abs(int(tile_a[1])-int(tile_b[1]))+1))
    area_shapely = Polygon([
        (int(tile_a[0]), int(tile_a[1])),
        (int(tile_a[0]), int(tile_b[1])+1),
        (int(tile_b[0])+1, int(tile_b[1])+1),
        (int(tile_b[0])+1, int(tile_a[1])),
        (int(tile_a[0]), int(tile_a[1]))
    ]).area
    print(area_self, area_shapely)
    '''
    return (
        (abs(int(tile_a[0])-int(tile_b[0]))+1) *
        (abs(int(tile_a[1])-int(tile_b[1]))+1)
    )

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

tiles_sorted_xy = sorted(sorted(tiles_int, key = lambda x: x[0]), key = lambda x: x[1])
print("Tiles (x-y):", tiles_sorted_xy)

# Polygon construction (large floor)
next_tile = tiles_sorted_xy.pop(0)
is_follow_horizontal = True
polygon_tiles = [next_tile]
for tile_index in range(len(tiles_int)):
    #print("Drawing", next_tile)
    for pop_index in range(len(tiles_sorted_xy)):
        if is_follow_horizontal:
            if tiles_sorted_xy[pop_index][1] == next_tile[1]:
                next_tile = tiles_sorted_xy.pop(pop_index)
                polygon_tiles.append(next_tile)
                is_follow_horizontal = False
                break
        else:
            if tiles_sorted_xy[pop_index][0] == next_tile[0]:
                next_tile = tiles_sorted_xy.pop(pop_index)
                polygon_tiles.append(next_tile)
                is_follow_horizontal = True
                break
print("Polygon Indices:", polygon_tiles)
polygon_floor = Polygon(polygon_tiles)
print("Polygon", polygon_floor)
#plt.plot(*polygon_floor.exterior.xy)
#p = gpd.GeoSeries(polygon_floor)
#p.plot()
#plt.show()

# create all rectangles possible and their area
tile_areas = []
for tile_a_index in range(0, len(tiles)):
    for tile_b_index in range(tile_a_index+1, len(tiles)):
        area_tuple = []
        area_tuple.append(rectangle_area(tiles[tile_a_index], tiles[tile_b_index]))
        area_tuple.append([tile_a_index, tile_b_index])
        tile_areas.append(area_tuple)
print("Areas:", tile_areas)

# create polygons of all rectangles
valid_tile_areas = []
for area_tuple in sorted(tile_areas, key=lambda x: x[0], reverse=True):
    if tile_index != area_tuple[1][0] and tile_index != area_tuple[1][1]:
        tiles_rectangle = [
            tiles_int[area_tuple[1][0]],
            tiles_int[area_tuple[1][1]]
        ]
        tiles_rectangle_sorted_xy = sorted(sorted(tiles_rectangle, key=lambda x: x[0]), key=lambda x: x[1])
        #print("Rectangle Tiles (x-y):", tiles_rectangle_sorted_xy)
        rectangle_coordinates = []
        rectangle_coordinates.append([tiles_rectangle_sorted_xy[0][0], tiles_rectangle_sorted_xy[0][1]])
        rectangle_coordinates.append([tiles_rectangle_sorted_xy[0][0], tiles_rectangle_sorted_xy[1][1]])
        rectangle_coordinates.append([tiles_rectangle_sorted_xy[1][0], tiles_rectangle_sorted_xy[1][1]])
        rectangle_coordinates.append([tiles_rectangle_sorted_xy[1][0], tiles_rectangle_sorted_xy[0][1]])
        #print(rectangle_coordinates)
        polygon_rectangle = Polygon(rectangle_coordinates)

        if polygon_rectangle.within(polygon_floor):
            print("Rectangle", polygon_rectangle, "found")
            print("Solution:", area_tuple[0])
            break

            #if is_contained_in_area(floor, tiles[area_tuple[1][0]], tiles[area_tuple[1][1]]):
                #if area_rectangle.within(area_floor):
                #    print("we are in")
                #    valid_tile_areas.append(area_tuple)
                #else:
                #    print("we are not in")

#max_area = 0
#max_area = valid_tile_areas[0][0]
#print("Solution:", max_area)
