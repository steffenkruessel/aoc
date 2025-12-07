
with open("input.txt", "r") as file:
    manifold = []
    for line in file:
        manifold.append(line.strip("\n\r"))
    
    # replace start with a tachyon
    manifold[0] = manifold[0].replace("S", "|")
    print(manifold)
    
    # do not touch last row as it does not contain splitter
    for row_index in range(len(manifold) - 1):
        for char_index in range(1, len(manifold[row_index]) - 1):
            if manifold[row_index][char_index] == "|":
                # tachyon found
                #print("Tachyon found at", row_index, char_index)
                # for each tachyon we check the next row
                if manifold[row_index + 1][char_index] == "^":
                    # for each splitter, the next row will split the tachyon
                    manifold[row_index + 1] = manifold[row_index + 1][:char_index - 1] + "|^|" + manifold[row_index + 1][char_index + 2:]
                else:
                    manifold[row_index + 1] = manifold[row_index + 1][:char_index] + "|" + manifold[row_index + 1][char_index + 1:]
            elif manifold[row_index][char_index] == "^":
                # splitter found
                #print("Splitter found at", row_index, char_index)
                continue
            else:
                # free space found
                continue
            
            #print(manifold[row_index])
            
    print(manifold)
    
    split_total = 0
    for row_index in range(1, len(manifold) - 1):
        for char_index in range(1, len(manifold[row_index])):
            if manifold[row_index][char_index] == "^" and manifold[row_index - 1][char_index] == "|":
                split_total += 1
    
    print("Solution:", split_total)
