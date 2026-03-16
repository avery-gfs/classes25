l = [3, 1, 4, 1, 5, 9, 2, 6, 5, 4]

for i in range(10):
    for j in range(i, 10):
        if l[j] < l[i]:
            tmp = l[i]
            l[i] = l[j]
            l[j] = tmp

print(l)

# Hint:
#
# We could have written our code like this:

# for r0 in range(10):
#     for r1 in range(r0, 10):
#         r2 = l[r0]
#         r3 = l[r1]
#         r3 = r3 < r2
#         if r3 == 0:
#             pass
#         else:
#             r3 = l[r1]
#             l[r0] = r3
#             l[r1] = r2
