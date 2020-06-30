a = [23, 65, 78, 98, 14, 3, 5, 15]
a.sort()
print(a)

x = [12, 29, 65, 45, 37, 89, 94, 68, 75]

for i in range(len(x)-1, 0, -1):
    for j in range(i):
        if x[j] > x[j+1]:
            x[j], x[j+1] = x[j+1], x[j]

print("The list after sorting: ", x)
