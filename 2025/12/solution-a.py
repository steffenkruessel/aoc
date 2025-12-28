import re
import numpy as np

# rotate a package up to 3 times (each 90 degrees)
def package_rotate(package, times=1):
    #implement rotation
    return

# flip a package horizontally or vertically
def package_flip(package, horizontal=True, vertical=False):
    #implement flip
    return

with open("input.txt", "r") as file:
    is_package = False
    packages = []
    areas = []
    package_number = 0
    for line in file:
        # read packages
        data = line.strip("\n\r")

        if is_package:
            if data == "":
                # end of package
                #print("Package", package_number, "found with", packages[package_number])
                is_package = False
            else:
                package_row = []
                for character in data:
                    if character == "#": package_row.append(1)
                    else: package_row.append(0)
                packages[package_number].append(package_row)
        else:
            if re.search("^[0-9]*:", data):
                is_package = True
                package_number = int(data.strip(":")[0])
                #print("Package", package_number, "Start found")
                packages.append([])
            elif re.search("^[0-9]*x[0-9]*:", data):
                area = {}
                # get dimensions of each area
                dimensions = data.split(":")[0]
                (width, length) = dimensions.split("x")
                area.update({"dimensions": [int(width), int(length)]})

                package_quantities = data.split(": ")[1]
                quantities = []
                for package_quantity in package_quantities.split(" "):
                    quantities.append(int(package_quantity))
                area.update({"quantities": quantities})
                #print("Area", width, length, "found with", package_quantities)
                #print(area)
                areas.append(area)
    print("Packages:", packages)
    packages_np = []
    for package in packages:
        packages_np.append(np.array(package))
    #print(packages_np)
    print("Areas", areas)

# result
number_of_trees = 0

# check each area
print(len(areas), "Areas to be checked")
# remove all areas that are too small even in an optimal packaging
for area in areas.copy():
    A_area = area["dimensions"][0]*area["dimensions"][1]
    A_packages = 0
    for i in range(len(area["quantities"])):
        A_package = np.sum(packages_np[i])
        A_packages += A_package * area["quantities"][i]
        #print("Package", i, "(", A_package, ") used", area["quantities"][i], "times")

    if A_area < A_packages:
        #print("Area", area, "(", A_area, ") does not fit Packages (", A_packages, ")")
        areas.remove(area)
print(len(areas), "Areas to be checked after optimal fit")

# count (and remove) all areas that simply fit all packages regardless of shape (3x3 square)
for area in areas.copy():
    # width
    width_full = int(area["dimensions"][0] / 3)
    # length
    length_full = int(area["dimensions"][1] / 3)
    # area for tree that would fit 3x3 packages
    A_area = width_full * length_full
    # area if only put besides each other
    A_packages = np.sum(area["quantities"])

    if A_area >= A_package:
        areas.remove(area)
        number_of_trees += 1
print(len(areas), "Areas to be checked after worst fit")

print("Solution:", number_of_trees)