x = [12, 29, 65, 45, 37, 89, 94, 68, 75]

small = x[0]
big = x[0]

for i in range(len(x)):
    if x[i] < small:
        small = x[i]
    if x[i] > big:
        big = x[i]

print("The Largest number in the list is: ", big)
print("The Smallest number in the list is: ", small)
