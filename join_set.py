set = {"apple", "banana", "cherry"}
set1 = {"orange", "mango", "grape"}
set4 = {"kiwi", "pineapple"}
set2 = set.union(set1)
set5 = set4 | set2
set6 = set.intersection(set2)
set7 = set.symmetric_difference(set1)
set8 = set.difference(set1)
print(set6)
print(set5)
print(set2)
