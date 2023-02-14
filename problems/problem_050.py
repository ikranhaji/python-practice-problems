# Write a function that meets these requirements.
#
# Name:       halve_the_list
# Parameters: a single list
# Returns:    two lists, each containing half of the original list
#             if the original list has an odd number of items, then
#             the extra item is in the first list
#
# Examples:
#    * input: [1, 2, 3, 4]
#      result: [1, 2], [3, 4]
#    * input: [1, 2, 3]
#      result: [1, 2], [3]

def halve_the_list(list):
    list2 = []
    list3 = []
    length = len(list)
    middle = length // 2
    if length % 2 == 0:
        list2.append(list[:middle])
        list3.append(list[middle:])
    else:
        list2.append(list[:middle + 1])
        list3.append(list[middle + 1:])
    return list2, list3
