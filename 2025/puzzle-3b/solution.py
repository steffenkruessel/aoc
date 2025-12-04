with (open("input.txt") as file):
    bank_size = 12
    joltage = 0
    for line in file.readlines():
        # prepare string into int array
        print(line.rstrip())
        bank = list(map(int, line.rstrip()))

        highest_bank = []
        battery_index_latest = 0
        for battery_index in range(bank_size, 0, -1):
            #bank_slice = bank[battery_index_latest:(-battery_index + 1)]
            bank_slice = bank[battery_index_latest:(len(bank)-battery_index+1)]
            print(battery_index, battery_index_latest, (-battery_index + 1), bank_slice)

            bank_slice.sort()
            index = bank[battery_index_latest:].index(bank_slice[-1])
            highest_bank.append(bank[battery_index_latest+index])

            print("item", bank_slice[-1], "at position", index, "of", bank[battery_index_latest:])
            battery_index_latest += index + 1
        # only consider the first few digits as the rest naturally needs to fit for the whole number
        print(highest_bank)

        joltage += int(''.join(map(str, highest_bank)))

        print()

    print(joltage)
