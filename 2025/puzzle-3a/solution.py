with open("input.txt") as file:
    joltage = 0
    for line in file.readlines():
        # prepare string into int array
        print(line.rstrip())
        bank = list(map(int, line.rstrip()))

        # search for largest from left
        battery_first = bank[:-1]
        battery_first.sort()

        # search for the second largest
        battery_last = bank[bank.index(battery_first[-1])+1:]
        battery_last.sort()

        joltage += battery_first[-1]*10 + battery_last[-1]
        print(battery_first[-1] * 10 + battery_last[-1])

        print()

    print(joltage)
