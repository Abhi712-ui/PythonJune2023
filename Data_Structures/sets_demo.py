my_set = {1, 2, 3}

my_set.add(4)
print(my_set)  # Output: {1, 2, 3, 4}

my_set.remove(2)
print(my_set)  # Output: {1, 3, 4}

my_set.discard(5)  # No error raised if the element is not present

my_set = {1, 2, 3}
another_set = set([3, 4, 5])

set1 = {1, 2, 3}
set2 = {3, 4, 5}

union_set = set1 | set2
print(union_set)  # Output: {1, 2, 3, 4, 5}

intersection_set = set1 & set2
print(intersection_set)  # Output: {3}

difference_set = set1 - set2
print(difference_set)  # Output: {1, 2}

symmetric_difference_set = set1 ^ set2
print(symmetric_difference_set)  # Output: {1, 2, 4, 5}

is_subset = set1.issubset(set2)
print(is_subset)  # Output: False

is_superset = set1.issuperset(set2)
print(is_superset)  # Output: False

my_set = {1, 2, 3}

for item in my_set:
    print(item)
# Output: 1 2 3

set1 = {1, 2, 3}
set2 = {3, 4, 5}

union_set = set1.union(set2)
print(union_set)  # Output: {1, 2, 3, 4, 5}

intersection_set = set1.intersection(set2)
print(intersection_set)  # Output: {3}

difference_set = set1.difference(set2)
print(difference_set)  # Output: {1, 2}

symmetric_difference_set = set1.symmetric_difference(set2)
print(symmetric_difference_set)  # Output: {1, 2, 4, 5}

set_copy = set1.copy()
print(set_copy)  # Output: {1, 2, 3}

set1.clear()
print(set1)  # Output: set()

popped_element = set2.pop()
print(popped_element)  # Output: An arbitrary element from set2

set1.update(set2)
print(set1)  # Output: {3, 4, 5}

is_subset = set1.issubset(set2)
print(is_subset)  # Output: False

is_superset = set1.issuperset(set2)
print(is_superset)  # Output: False

frozen_set = frozenset([1, 2, 3])
# frozen_set.add(4)  # Raises an AttributeError, as frozensets are immutable
