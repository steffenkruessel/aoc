import csv
import math

class IDScanner:
    def __init__(self):
        pass

    @staticmethod
    def check_id(min_value, max_value):
        ids_incorrect = []

        digits_min_value = int(math.log10(min_value)) + 1
        digits_max_value = int(math.log10(max_value)) + 1
        print(min_value, max_value, digits_min_value, digits_max_value)

        if (digits_min_value % 2 != 0) and (digits_max_value == digits_min_value):
            print("Nothing to do\n")
            return ids_incorrect

        for value in range(min_value, max_value + 1):
            digits_value = int(math.log10(value)) + 1
            if digits_value % 2 == 0:
                value_left = int( value / (10**(digits_value/2)) )
                value_right = int( value % (10**(digits_value/2)) )
                #print(value, digits_value, value_left, value_right)
                if value_left == value_right:
                    ids_incorrect.append(value)

        print(ids_incorrect)
        return ids_incorrect


scanner = IDScanner()
results_sum = 0
results = []

with open("input.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        for id_range in row:
            # print(range)
            range_pos_hyphen = id_range.find('-')
            range_min = int(id_range[0:range_pos_hyphen])
            range_max = int(id_range[range_pos_hyphen + 1:])

            results_tmp = scanner.check_id(range_min, range_max)
            results.append(results_tmp)
            results_sum += sum(results_tmp)

print()
print(results)
print(results_sum)
