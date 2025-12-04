import numpy as np

def pretty_print(matrix):
    print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in matrix]))

def extend_outer_rim(storage):
    storage_rim = np.zeros((len(storage)+2, len(storage[0])+2))

    for i in range(len(storage)):
        for j in range(len(storage[0])):
            storage_rim[i+1, j+1] = storage[i][j]

    return storage_rim.tolist()
    #print(my_storage)
    # create an outer rim of zeros to ease the calculation later on
    '''
    storage_row_zeros = []
    for i in range(0, len(storage) + 2):
        storage_row_zeros.append(0)
    storage.append(storage_row_zeros)

    storage_row.append(0)
    for row in storage:
        # fill the actual contents
        storage_row = []
        for symbol in line.rstrip():
            storage_row.append(0 if symbol == "." else 1)
        storage.append(storage_row)

    storage_row.append(0)

    # create an outer rim of zeros to ease the calculation later on
    storage_row_zeros = []
    for i in range(0, len(line.rstrip()) + 2):
        storage_row_zeros.append(0)
    storage.append(storage_row_zeros)
    '''

def move_paper(storage):
    storage_matrix = np.matrix(extend_outer_rim(storage))
    #print(storage_matrix)
    # due to the outer rim, we start from 1 and not 0 and run for 1 less than the length
    num_of_accessible_papers = 0
    # matrix that indicates all papers that will get moved
    storage_move = []
    for row_number in range(0, len(storage)):
        storage_row_move = []
        for item_number in range(0, len(storage[row_number])):
            # check the surrounding
            if storage[row_number][item_number]:
                storage_slice = storage_matrix[row_number:(row_number+3),
                                                item_number:(item_number+3)]
                #print(storage_slice)
                adjacency = np.sum(storage_slice) - 1
                # print("Paper-Roll", row_number, item_number, adjacency)
                if adjacency < 4:
                    storage_row_move.append(1)
                    num_of_accessible_papers += 1
                else:
                    storage_row_move.append(0)
            else:
                storage_row_move.append(0)
        storage_move.append(storage_row_move)

    # pretty_print(storage_move)

    if num_of_accessible_papers != 0:
        return move_paper((np.array(storage) - np.array(storage_move)).tolist()) + num_of_accessible_papers
    else:
        return 0


with (open("input.txt") as file):
    # construct the storage as a matrix of zeros and ones
    storage = []
    for line in file.readlines():
        # fill the actual contents
        storage_row = []
        for symbol in line.rstrip():
            storage_row.append(0 if symbol == "." else 1)
        storage.append(storage_row)

    pretty_print(storage)

    amount_of_moves = move_paper(storage)
    print()
    print("Overall Number of Rolls:", amount_of_moves)