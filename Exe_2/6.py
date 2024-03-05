# Define two sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Display the sets
print("Set 1:", set1)
print("Set 2:", set2)

# Set Operations
union_set = set1.union(set2)  # Union of sets
intersection_set = set1.intersection(set2)  # Intersection of sets
difference_set1_minus_set2 = set1.difference(set2)  # Elements in set1 but not in set2
difference_set2_minus_set1 = set2.difference(set1)  # Elements in set2 but not in set1
symmetric_difference_set = set1.symmetric_difference(set2)  # Elements in either set but not in both

# Validation Operations
is_subset = set1.issubset(set2)  # Check if set1 is a subset of set2
is_superset = set1.issuperset(set2)  # Check if set1 is a superset of set2
is_disjoint = set1.isdisjoint(set2)  # Check if set1 and set2 have no common elements

# Display the results
print("\nSet Operations:")
print("Union:", union_set)
print("Intersection:", intersection_set)
print("Difference (set1 - set2):", difference_set1_minus_set2)
print("Difference (set2 - set1):", difference_set2_minus_set1)
print("Symmetric Difference:", symmetric_difference_set)

print("\nValidation Operations:")
print("Is set1 a subset of set2:", is_subset)
print("Is set1 a superset of set2:", is_superset)
print("Are set1 and set2 disjoint:", is_disjoint)
