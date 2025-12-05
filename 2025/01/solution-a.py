code = 0

num_lines = sum(1 for _ in open("input.txt"))
print(num_lines)

# initialize dial
dial = 100*num_lines+50
print(dial)

with open("input.txt") as file:
    for line in file:
        if line[0] == "L":
            # turn dial left (-)
            dial -= int(line.rstrip()[1:])
        else:
            # turn dial right (+)
            dial += int(line.rstrip()[1:])

        print(dial)
        # calculate code
        if dial % 100 == 0: code += 1

print(code)