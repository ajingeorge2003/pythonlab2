def merging_Dict(*args):
    merged_dict = {}
    for dictionary in args:
        merged_dict.update(dictionary)
    return merged_dict

def common_keys(*args):
    if not args:
        return set()
    common_keys_set = set(args[0].keys())
    for dictionary in args[1:]:
        common_keys_set.intersection_update(dictionary.keys())
    return common_keys_set

def invert_dict(d):
    inverted_dict = {}
    for key, value in d.items():
        if value in inverted_dict:
            if type(inverted_dict[value]) is list:
                inverted_dict[value].append(key)
            else:
                inverted_dict[value] = [inverted_dict[value], key]
        else:
            inverted_dict[value] = key
    return inverted_dict
