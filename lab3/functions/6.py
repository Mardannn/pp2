#Write a function find_common_elements that takes two lists as parameters and returns a new list containing common elements between them.
def find_common_elements(list1, list2):
    return list(set(list1) & set(list2))

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
common_elements = find_common_elements(list1, list2)
print(common_elements)