import module_SetOperations as mso

s1 = [1, 2, 3]
s2 = [3, 4, 5]
    
print("Original sets:")
print("s1:", s1)
print("s2:", s2)
    

mso.add_element(s1, 4)
print("\nAfter adding 4 to s1:", s1)
    

mso.remove_element(s1, 2)
print("After removing 2 from s1:", s1)
    

union, intersection = mso.union_and_intersection(s1, s2)
print("\nUnion of s1 and s2:", union)
print("Intersection of s1 and s2:", intersection)
    

diff = mso.difference(s1, s2)
print("\nDifference s1 - s2:", diff)
    

subset_check = mso.is_subset(s1, s2)
print("\nIs s1 a subset of s2?", subset_check)
    

length = mso.set_length(s1)
print("\nLength of s1:", length)
    

sym_diff = mso.symmetric_difference(s1, s2)
print("\nSymmetric difference of s1 and s2:", sym_diff)
    

p_set = mso.power_set(s1)
print("\nPower set of s1:", p_set)
    

u_subsets = mso.unique_subsets(s1)
print("\nUnique subsets of s1:", u_subsets)

''' 
Original sets:
s1: [1, 2, 3]
s2: [3, 4, 5]

After adding 4 to s1: [1, 2, 3, 4]
After removing 2 from s1: [1, 3, 4]

Union of s1 and s2: [1, 3, 4, 5]
Intersection of s1 and s2: [3, 4]

Difference s1 - s2: [1]

Is s1 a subset of s2? False

Length of s1: 3

Symmetric difference of s1 and s2: [1, 5]

Power set of s1: [[], [1], [3], [1, 3], [4], [1, 4], [3, 4], [1, 3, 4]]

Unique subsets of s1: [[], [1], [3], [1, 3], [4], [1, 4], [3, 4], [1, 3, 4]]
'''