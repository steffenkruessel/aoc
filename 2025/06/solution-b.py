
numbers = []
calculations = []
with open("input.txt", "r") as file:
    lines = []
    for line in file:
        print("Line:", line)
        lines.append(line.strip("\n\r"))
    print(lines)

    max_len = len(max(lines, key=len))

    # put leading and tailing zeros in empty spaces
    operation_indices = []
    for index in range(len(lines[-1])):
        if lines[-1][index] != " ":
            print("Index:", index)
            operation_indices.append(index)
    operation_indices.append(max_len+1)
    
for line in lines:
    for item in line:
        if item == "+" or item == "*":
            calculations.append(item)
        elif item == "":
            continue

for line in lines[:-1]:
    print(line)
    numbers.append(line)

print(numbers)
print(calculations)

result = 0
for i in range(len(calculations)):
    sum_tmp, product_tmp = 0, 0
    
    cepha_numbers = []
    for a in range(operation_indices[i], operation_indices[i+1]-1):
        cepha_number = ""
        for line in numbers:
            cepha_number += line[a] 
        print("Cepha Number:", cepha_number)
        cepha_numbers.append(cepha_number)
    
    calculation = calculations[i]
    if calculation == "+":
        print("ADDITION", operation_indices[i], operation_indices[i+1]-1)
        sum_tmp = 0

        for number in cepha_numbers:
            print("add", number, "to", sum_tmp)
            sum_tmp += int(number)
        result += sum_tmp
    elif calculation == "*":
        print("MULTIPLICATION", operation_indices[i], operation_indices[i+1]-1)
        product_tmp = 1

        for number in cepha_numbers:
            print("multiply", number, "by", product_tmp)
            product_tmp *= int(number)
        result += product_tmp
print(result)
