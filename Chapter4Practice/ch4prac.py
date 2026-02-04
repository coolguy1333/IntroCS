# ax^2 + bx + c

a = float(input("What is the a value of your quadratic?"))
b = float(input("What is the b value of your quadratic?"))
c = float(input("What is the c value of your quadratic?"))

# (-b +/- Root(b^2-4ac)) / (2a)

discriminant = b * b - 4 * a * c
solution1 = (-1 * b + discriminant ** 0.5) / (2 * a)
solution2 = (-1 * b - discriminant ** 0.5) / (2 * a)

print("Solution 1 is ",solution1)
print("Solution 2 is ",solution2)