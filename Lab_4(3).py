my_list = [12, 45, 23, 56, -546, 34]
transformation = [i*(i-10) for i in my_list]
squares = [i**2 for i in my_list]
print("Transformation x*(x-10): {}".format(transformation))
print("Squares x^2: {}".format(squares))
##squares = []
##for i in my_list:
##    x = x * (x - 10)
