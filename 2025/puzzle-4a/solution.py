import numpy as np

with (open("input.txt") as file):
    # construct the storage as a matrix of zeros and ones
    row = 0
    storage = []
    for line in file.readlines():
        # create an outer rim of zeros to ease the calculation later on
        if not storage:
            storage_row_zeros = []
            for i in range(0, len(line.rstrip())+2):
                storage_row_zeros.append(0)
            storage.append(storage_row_zeros)

        # fill the actual contents
        column = 0
        storage_row = []
        storage_row.append(0)
        for symbol in line.rstrip():
            storage_row.append(0 if symbol == "." else 1)
            column += 1
        storage.append(storage_row)
        storage_row.append(0)
        row += 1

    # create an outer rim of zeros to ease the calculation later on
    storage_row_zeros = []
    for i in range(0, len(line.rstrip()) + 2):
        storage_row_zeros.append(0)
    storage.append(storage_row_zeros)

    #print(storage)
    print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in storage]))

    storage_matrix = np.matrix(storage)
    # due to the outer rim, we start from 1 and not 0 and run for 1 less than the length
    num_of_accessible_papers = 0
    for row_number in range(1, len(storage)-1):
        for item_number in range(1, len(storage[row_number])-1):
            # check the surrounding
            if storage[row_number][item_number]:
                storage_slice = storage_matrix[row_number - 1:row_number + 1 + 1,
                                                item_number - 1:item_number + 1 + 1]
                print(storage_slice)
                adjacency = np.sum(storage_slice) - 1
                print("Paper-Roll", row_number, item_number, adjacency)
                if adjacency < 4: num_of_accessible_papers += 1

    print()
    print("Overall Number of Rolls:", num_of_accessible_papers)