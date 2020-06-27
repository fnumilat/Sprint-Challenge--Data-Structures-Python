import time
from bst import BSTNode

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements

# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# using binary search tree to improve the runtime
bst = BSTNode('names')

for names in names_1: # O(n)
    bst.insert(names) # O(log n)
for names in names_2: # O(n)
    if bst.contains(names): # O(log n)
        duplicates.append(names) # O(1)



# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

# Using sorting and index comparison to find repeated values in the sorted list
# names = names_1 + names_2  # O(2n)
# names.sort()  # O(nlogn)
# counter = 1  # O(1)
# repeat = ""  # O(1)
# for idx in range(len(names)):  # O(n + k)

#     current_name = names[idx]  # O(1)
#     if idx > 0:  # O(1)
#         if names[idx - 1] == names[idx]:  # O(1)
#             counter += 1  # O(1)
#             repeat = current_name  # O(1)
#             if counter >= 2:  # O(1) and prevents multiple duplicates of same name
#                 duplicates.append(names[idx])  # O(1)
#         else:
#             # Reset counter, both at O(1)
#             counter = 1
            # repeat = ""


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# the provided loop runtime: 9.546212673187256 seconds ---> O(n^2)
# the improved loop runtime: 0.14564204216003418 seconds ---> O(n log n)
# the strectch runtime: 0.1765589714050293 seconds ---> O(n log n)
