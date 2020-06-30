x = input("Please enter your First followed by your last name separated by space \n")
a = x.split(" ")
b = " ".join(a[::-1])
print(b)
