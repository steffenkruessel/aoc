numbers = []
calculations = []
with open("input.txt", "r") as file:
    for line in file:
        #print("Line:", line)
        
        numbers_row = []
        for item in line.rstrip().split():
            #print("Item:", item)
            if item == "+" or item == "*":
                calculations.append(item)
            elif item == "":
                continue
            else:
                numbers_row.append(int(item))
        #print("Row:", numbers_row)
        if numbers_row:
            numbers.append(numbers_row)

    print(numbers)
    print(calculations)

    result = 0
    for i in range(len(calculations)):
        sum_tmp, product_tmp = 0, 0
        calculation = calculations[i]
        if calculation == "+":
            sum_tmp = 0
            for j in range(len(numbers)):
                number = numbers[j][i]
                print("add", number, "to", sum_tmp)
                sum_tmp += number
            result += sum_tmp
        elif calculation == "*":
            product_tmp = 1
            for j in range(len(numbers)):
                number = numbers[j][i]
                print("multiply", number, "by", product_tmp)
                product_tmp *= number
            result += product_tmp
    print(result)
