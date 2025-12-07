from array import array

with open("input.txt", "r") as file:
    manifold = []
    for line in file:
        manifold_row = []
        for character in line.strip("\n\r"):
            if character == "S":
                manifold_row.append("1")
            else:
                manifold_row.append(character)
        manifold.append(manifold_row)

    #for item in manifold:
    #    print(item)
    
    # replace start with a tachyon
    print(manifold)
    
    # do not touch last row as it does not contain splitter
    for row_index in range(len(manifold) - 1):
        for char_index in range(0, len(manifold[row_index])):
            if manifold[row_index][char_index] != "." and manifold[row_index][char_index] != "^":
                # tachyon found
                #print("Tachyon found at", row_index, char_index)
                timelines_old = int(manifold[row_index][char_index])
                # for each tachyon we check the next row
                if manifold[row_index + 1][char_index] == "^":
                    # for each splitter, the next row will split the tachyon
                    timelines_new_left = 0
                    if manifold[row_index + 1][char_index - 1] != ".":
                        timelines_new_left += int(manifold[row_index + 1][char_index-1])
                    
                    timelines_new_right = 0
                    if manifold[row_index + 1][char_index + 1] != ".":
                        timelines_new_right += int(manifold[row_index + 1][char_index + 1])

                    #print("left", ''.join(str(timelines_old+timelines_new_left)), "right", str(timelines_old+timelines_new_right))
                    #manifold[row_index + 1] = (manifold[row_index + 1][:char_index - 1] +
                    #       list((str(timelines_old + timelines_new_left) + "^" + str(timelines_old + timelines_new_right))) +
                    #       manifold[row_index + 1][char_index + 2:])
                    #print("start:", manifold[row_index + 1])
                    manifold_tmp = manifold[row_index+1][:char_index-1]
                    manifold_tmp.append(str(timelines_old + timelines_new_left))
                    manifold_tmp.append("^")
                    manifold_tmp.append(str(timelines_old + timelines_new_right))
                    manifold_tmp += manifold[row_index + 1][char_index + 2:]
                    manifold[row_index + 1] = manifold_tmp
                    #print("stopp:", manifold[row_index + 1])
                else:
                    #print("new-line", manifold[row_index+1])
                    timelines_new_middle = 0
                    if manifold[row_index + 1][char_index] != ".":
                        timelines_new_middle += int(manifold[row_index + 1][char_index])
                    #print("will do", manifold[row_index + 1][:char_index], manifold[row_index + 1][char_index + 1:])

                    manifold_tmp = list()
                    manifold_tmp += manifold[row_index + 1][:char_index]
                    manifold_tmp.append(str(timelines_old+timelines_new_middle))
                    #print(timelines_old, timelines_new_middle, str(timelines_old+timelines_new_middle))
                    manifold_tmp += manifold[row_index + 1][char_index + 1:]
                    manifold[row_index + 1] = manifold_tmp
            
        print(manifold[row_index])
        #print("row")
        #print(manifold[row_index+1])
        #print("done")
            
    print(manifold)
    
    timelines = 0
    for item in manifold[-2]:
        if item != "^" and item != ".":
            timelines += int(item)
    
    print("Timelines:", timelines)
    
    '''
    timeline_total = 1
    for row_index in range(1, len(manifold) - 1):
        timeline_row = 0
        for char_index in range(1, len(manifold[row_index])):
            if manifold[row_index][char_index] == "^" and manifold[row_index - 1][char_index] == "|":
                timeline_row += 1
        timeline_total += 2*timeline_row
    
    print("Solution:", timeline_total)
    '''
