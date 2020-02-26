import math

while True:
    try:
        a = int(input("Please enter 'a' value: "))
        break
    except ValueError:
        print("The value must be an integer.")
        continue

while True:
    try:
        b = int(input("Please enter 'b' value: "))
        break
    except ValueError:
        print("The value must be an integer.")
        continue

c_pow2 = a**2 + b**2
c = math.sqrt(c_pow2)

print("Pythagorean theorem: ")
print("\tc^2 = a^2 + b^2")
print("\t{} = {}^2 + {}^2".format(c_pow2, a, b))
print()
print("Answer: c = {}".format(c))
