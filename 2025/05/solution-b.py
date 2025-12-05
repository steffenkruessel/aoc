import numpy as np

ingredients_fresh = []
with (open("input.txt") as file):
    for line in file.readlines():
        if line.rstrip() == "":
            break
        ingredients_fresh.append(line.rstrip())

    print(ingredients_fresh)

ingredients_fresh_total = []
for ingredient_range in ingredients_fresh:
    print("handling", ingredient_range)
    ingredient_ids = ingredient_range.split("-")
    ingredient_min = int(ingredient_ids[0])
    ingredient_max = int(ingredient_ids[1])

    new_min = ingredient_min
    new_max = ingredient_max
    ingredients_to_be_removed = []
    for i in range(len(ingredients_fresh_total)):
        is_ingredient_in_range = False
        print("analyzing:", ingredients_fresh_total[i])
        ingredient_total_ids = ingredients_fresh_total[i].split("-")
        ingredient_total_min = int(ingredient_total_ids[0])
        ingredient_total_max = int(ingredient_total_ids[1])

        # test if new range attaches/overlaps to already existing range
        # new range starts before old range
        if new_min < ingredient_total_min <= new_max:
            print("   new range starts before old range", new_min, new_max)
            is_ingredient_in_range = True
        # new range starts in between old range
        if ingredient_total_min <= new_min <= ingredient_total_max:
            print("   new range starts in between old range", new_min, new_max)
            new_min = ingredient_total_min
            is_ingredient_in_range = True
        # new range ends behind old range
        if new_max > ingredient_total_max >= new_min:
            print("   new range ends behind old range", new_min, new_max)
            is_ingredient_in_range = True
        # new range ends in between old range
        if ingredient_total_max >= new_max >= ingredient_total_min:
            print("   new range ends in between old range", new_min, new_max)
            new_max = ingredient_total_max
            is_ingredient_in_range = True

        if is_ingredient_in_range:
            ingredients_to_be_removed.append(ingredients_fresh_total[i])

    ingredients_fresh_total = [x for x in ingredients_fresh_total if x not in ingredients_to_be_removed]
    ingredients_fresh_total.append(str(new_min) + "-" + str(new_max))
    print("---current state---", ingredients_fresh_total)

num_of_ingredients = 0
for ingredient_range in ingredients_fresh_total:
    ingredient_range_ids = ingredient_range.split("-")
    num_of_ingredients += int(ingredient_range_ids[1])+1 - int(ingredient_range_ids[0])

print(ingredients_fresh_total)
print()
print("Overall Number of Ingredients:", num_of_ingredients)