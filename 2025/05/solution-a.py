import numpy as np

ingredients_fresh = []
ingredients_available = []
ingredients = []
with (open("input.txt") as file):
    is_fresh_section_over = False
    for line in file.readlines():
        if line.rstrip() == "":
            is_fresh_section_over = True
        if not is_fresh_section_over:
            ingredients_fresh.append(line.rstrip())
        elif line.rstrip() == "":
            continue
        else:
            ingredients_available.append(int(line.rstrip()))
    print(ingredients_fresh)
    print(ingredients_available)

available_ingredients = 0
for ingredient_available in ingredients_available:
    for range_fresh in ingredients_fresh:
        print("handling", range_fresh)
        ingredient_ids = range_fresh.split("-")
        ingredient_min = int(ingredient_ids[0])
        ingredient_max = int(ingredient_ids[1])

        if ingredient_available >= ingredient_min and ingredient_available <= ingredient_max:
            available_ingredients += 1
            break

print()
print("Overall Number of Ingredients:", available_ingredients)