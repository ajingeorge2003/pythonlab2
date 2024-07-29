def add_element(s, element):
    if element not in s:
        s.append(element)

def remove_element(s, element):
    if element in s:
        s.remove(element)

def union_and_intersection(s1, s2):
    union = s1[:]
    intersection = []
    for elem in s2:
        if elem not in s1:
            union.append(elem)
        else:
            intersection.append(elem)
    return union, intersection

def difference(s1, s2):
    diff = []
    for elem in s1:
        if elem not in s2:
            diff.append(elem)
    return diff

def is_subset(s1, s2):
    for elem in s1:
        if elem not in s2:
            return False
    return True

def set_length(s):
    count = 0
    for _ in s:
        count += 1
    return count

def symmetric_difference(s1, s2):
    sym_diff = []
    for elem in s1:
        if elem not in s2:
            sym_diff.append(elem)
    for elem in s2:
        if elem not in s1:
            sym_diff.append(elem)
    return sym_diff

def power_set(s):
    p_set = [[]]
    for elem in s:
        new_subsets = [subset + [elem] for subset in p_set]
        p_set.extend(new_subsets)
    return p_set

def unique_subsets(s):
    p_set = power_set(s)
    unique_subs = []
    for subset in p_set:
        subset = sorted(subset)
        if subset not in unique_subs:
            unique_subs.append(subset)
    return unique_subs