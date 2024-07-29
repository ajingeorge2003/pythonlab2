from module_DictOperations import merging_Dict, common_keys, invert_dict

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 2, 'c': 4, 'd': 5}
dict3 = {'c': 3, 'd': 5, 'e': 6}

print("Original dictionaries:")
print("dict1:", dict1)
print("dict2:", dict2)
print("dict3:", dict3)


merged = merging_Dict(dict1, dict2, dict3)
print("\nMerged dictionary:", merged)


common = common_keys(dict1, dict2, dict3)
print("\nCommon keys:", common)


inverted = invert_dict(dict1)
print("\nInverted dictionary (dict1):", inverted)


inverted2 = invert_dict(merged)
print("\nInverted merged dictionary:", inverted2)
