def main():
    """Do This Now - parallel lists"""

    name_to_age = {"Bill": 21, "Jane": 34, "Sven": 56}
    name = input("Name: ")
    age = int(input("Age: "))
    name_to_age[name] = age
    max_length = max(len(name) for name in list(name_to_age.keys()))
    for name, age in name_to_age.items():
        print(f"{name:{max_length}} -\t{age:3}")

    # ages = list(name_to_age.values())
    # ages.sort()
    # print(ages)
    # for name in name_to_age:
    #     print(f"{name} is {name_to_age[name]}")

    # run_tests()


main()

# def run_tests():
#     i = 0
#     names = ["Bill", "Jane", "Sven"]
#     ages = [21, 34, 56]
#     # print(names[i], "is", ages[i], "years old")
#     print(find_oldest(names, ages))
#
#
# def find_oldest(names, ages):
#     # i = ages.index(max(ages))
#     # return names[ages.index(max(ages))]
#     oldest_age = -1
#     oldest_index = -1
#     for i, age in enumerate(ages):
#         if age > oldest_age:
#             oldest_age = age
#             oldest_index = i
#     return names[oldest_index]
