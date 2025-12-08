import math

def straight_line_distance(box_a, box_b):
    return math.sqrt(
        (int(box_b[0]) - int(box_a[0])) ** 2 +
        (int(box_b[1]) - int(box_a[1])) ** 2 +
        (int(box_b[2]) - int(box_a[2])) ** 2
    )

iterations = 1000
top_x = 3

junction_boxes = []
with open("input.txt", "r") as file:
    for line in file:
        junction_boxes.append(line.strip("\n\r").split(","))
print("Junction Boxes:", junction_boxes)

box_distances = []
for box_a_index in range(0, len(junction_boxes)):
    for box_b_index in range(box_a_index+1, len(junction_boxes)):
        distance_tuple = []
        distance_tuple.append(straight_line_distance(junction_boxes[box_a_index], junction_boxes[box_b_index]))
        distance_tuple.append([box_a_index, box_b_index])
        box_distances.append(distance_tuple)
print("Distances:", box_distances)

circuits = []
for junction_index in range(0, len(junction_boxes)):
    circuits.append([int(junction_index)])
print("Circuits:", circuits)

iteration = 0
for distance_tuple in sorted(box_distances, key=lambda x: x[0]):
    if iteration >= iterations: break
    print(distance_tuple)
    circuit_a, circuit_b = -1, -1
    for circuit_index in range(0, len(circuits)):
        for circuit in circuits[circuit_index]:
            if distance_tuple[1][0] == circuit: circuit_a = circuit_index
            if distance_tuple[1][1] == circuit: circuit_b = circuit_index

    if circuit_a != circuit_b:
        circuits[circuit_a] += circuits[circuit_b]
        circuits.pop(circuit_b)
    #print("New Circuit", circuit_a, circuit_b)

    iteration += 1
print("Circuits:", circuits)

junction_sizes = []
for circuit in circuits:
    junction_sizes.append(len(circuit))
print(junction_sizes)
junction_sizes.sort(reverse=True)
print(junction_sizes)

product_junctions = 1
for i in range(0, top_x):
    product_junctions *= junction_sizes[i]

print("Solution:", product_junctions)