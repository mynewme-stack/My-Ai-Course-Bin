# Group Pairs into a Tuple of Tuples
def group_pair (my_list):
    if len(my_list)% 2 != 0:
        raise ValueError('Incorrect number of elements.')
    pairs = tuple(zip(my_list[0::2],my_list[1::2]))
    return pairs
data = [ 'Name:','Abdul Rabb','Age:','20']
print(group_pair(data))