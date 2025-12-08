import math

def straight_line_distance(box_a, box_b):
    return math.sqrt(
        (int(box_b[0]) - int(box_a[0])) ** 2 +
        (int(box_b[1]) - int(box_a[1])) ** 2 +
        (int(box_b[2]) - int(box_a[2])) ** 2
    )

junction_boxes = []
with open("input.txt", "r") as file:
    for line in file:
        junction_boxes.append(line.strip("\n\r").split(","))
print("Junction Boxes:", junction_boxes)

box_distances = []
for box_a_index in range(0, len(junction_boxes)):
    for box_b_index in range(box_a_index+1, len(junction_boxes)):
        distance_tuple = [straight_line_distance(junction_boxes[box_a_index], junction_boxes[box_b_index]),
                          [box_a_index, box_b_index]]
        box_distances.append(distance_tuple)
print("Distances:", box_distances)
print("Distances (ordered):", sorted(box_distances, key=lambda x: x[0], reverse=True))

circuits = []
for junction_index in range(0, len(junction_boxes)):
    circuits.append([int(junction_index)])
print("Circuits:", circuits)

last_circuit_a, last_circuit_b = 0, 0
for distance_tuple in sorted(box_distances, key=lambda x: x[0]):
    if len(circuits) <= 1: break
    #print(distance_tuple)
    circuit_a, circuit_b = -1, -1
    for circuit_index in range(0, len(circuits)):
        for circuit in circuits[circuit_index]:
            if distance_tuple[1][0] == circuit:
                circuit_a = circuit_index
                last_circuit_a = distance_tuple[1][0]
                print("Distance A:", last_circuit_a)
            if distance_tuple[1][1] == circuit:
                circuit_b = circuit_index
                last_circuit_b = distance_tuple[1][1]
                print("Distance B:", last_circuit_b)

    if circuit_a != circuit_b:
        circuits[circuit_a] += circuits[circuit_b]
        circuits.pop(circuit_b)
    #print("New Circuit", circuit_a, circuit_b)
print("Circuits:", circuits)
print("Junctions:", junction_boxes[last_circuit_a][0], junction_boxes[last_circuit_b][0])

product_junctions = int(junction_boxes[last_circuit_a][0]) * int(junction_boxes[last_circuit_b][0])
print("Solution:", product_junctions)