import csv
import math



class IDScanner:
    def __init__(self):
        pass

    @staticmethod
    def check_id(min_value, max_value):
        ids_incorrect = []

        for value in range(min_value, max_value + 1):
            value_num_of_digits = int(math.log10(value)) + 1
            value_digits = [int(digit) for digit in str(value)]
            #print("digits", value_digits)

            for divisor in range(1, value_num_of_digits // 2 + 1):
                # check if the "string" of digits can be divided fully by the divisor
                if value_num_of_digits % divisor != 0:
                    continue

                #print("divisor", divisor)

                # split the number into the even parts
                value_parts = []
                for position in range(0, value_num_of_digits, divisor):
                    #print("position", position)
                    value_parts.append( int(''.join(map(str,value_digits[position:position+divisor]))) )

                #print(value_parts)

                if len(set(value_parts)) == 1:
                    ids_incorrect.append(value)

        # remember to list(set()) to get rid of duplicates beforehand
        #print(set(ids_incorrect))
        return set(ids_incorrect)


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
