def max_value(lst):
    if not lst:
        raise ValueError("List is empty")
    return max(lst)

def min_value(lst):
    if not lst:
        raise ValueError("List is empty")
    return min(lst)

def sum_list(lst):
    return sum(lst)

def average_list(lst):
    if not lst:
        raise ValueError("List is empty")
    return sum(lst) / len(lst)

def median_list(lst):
    if not lst:
        raise ValueError("List is empty")
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_lst[mid - 1] + sorted_lst[mid]) / 2
    else:
        return sorted_lst[mid]
