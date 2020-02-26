# generators
def number_generator(lst, stop=2):
    number = 0
    while number < stop:
        try:
            integer = int(lst.split(",")[number])
            yield integer*0.5
        except ValueError:
            print("The list was faulty!")
        number += 1

input_list = input("Enter a list of comma separated numbers:\n >> ")
generator = number_generator(input_list)

while True:
    try:
        print(next(generator))
    except StopIteration:
        break
