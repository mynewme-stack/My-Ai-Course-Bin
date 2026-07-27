# 1. Search for First Even in Nested Lists
def find_first(nested_list):
    for sub in nested_list:
        for number in sub:
            if number % 2 == 0:
                return number
                     
    return None

print(find_first([[1,3],[5,7,9],[7,9]]))
print(find_first([[2],[4,9]]))
print(find_first([[1,3],[5,7,9]]))