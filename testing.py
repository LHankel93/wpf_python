#
# 1. a list with all even numbers 
# 2. a list with all numbers dividable by 7
# 3. a list of numbers dividable by 9, in reverse order
# 4. a list all numbers, which start with an odd number

li = list(range(0,100))
l1 = li[::2]
l2 = li[7::7]
l3 = li[:8:-9]
l4 = li[::2]
print(l1)
print("\n")
print(l2)
print("\n")
print(l3)
print("\n")
print(l4)
