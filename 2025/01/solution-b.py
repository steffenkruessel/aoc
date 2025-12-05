code = 0

num_lines = sum(1 for _ in open("../puzzle-1b/input.txt"))

# initialize dial
dial = 1000*num_lines+50

with open("input.txt") as file:
    for line in file:
        if line[0] == "L":
            rotation = int(line.rstrip()[1:])

            dial_transformed = 0
            if (dial % 100) == 0:
                dial_transformed = (dial % 100)
            else:
                dial_transformed = ((dial % 100) - 100)

            code_delta = abs(int((dial_transformed - rotation) / 100))

            # first transform dial into the "negative counterpart" by -100
            # rotate left, full-division by 100
            print(line.rstrip() + ": " + str(code_delta))
            code += code_delta

            # turn dial left (-)
            dial -= rotation
        else:
            rotation = int(line.rstrip()[1:])

            code_delta = int(((dial % 100) + rotation) / 100)
            # first transform dial into the "negative counterpart" by -100
            # rotate left, full-division by 100
            print(line.rstrip() + ": " + str(code_delta))
            code += code_delta

            # turn dial right (+)
            dial += rotation

        print (str(dial) + " with code " + str(code))

print(code)