def find_subsets(lst) :
    if not lst:
        return [[]]
    subsets=find_subsets(lst[1:])
    return subsets+[[lst[0]]+subset for subset in subsets]

lst = [1, 2, 3]
subsets = find_subsets(lst)
print(subsets)