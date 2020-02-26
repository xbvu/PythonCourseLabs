digits=[]
while True:
    try:
        digits_input = input('Please enter comma separated digits: ')
        input_split_by_comma = digits_input.split(",")
        for digit in input_split_by_comma:
            digits.append(int(digit))
        break
    except ValueError:
        print("There is something wrong with the list you entered!")
        continue


sum_of_digits = sum(digits)
max_of_digits = max(digits)
min_of_digits = min(digits)
digits_2_to_4 = digits[1:4]
digits_count = len(digits)
values_greater_than_10 = [d for d in digits if d > 10]
ascending_digits = sorted(digits)
descending_digits = sorted(digits, reverse=True)
reversed_digits = list(reversed(digits))


print('Sum of digits: {}'.format(sum_of_digits))
print('Largest digit: {}'.format(max_of_digits))
print('Smallest digit: {}'.format(min_of_digits))
print('2nd to 4th digits: {}'.format(digits_2_to_4))
print('Digit count: {}'.format(digits_count))
print('Digits > 10: {}'.format(values_greater_than_10))
print('Ascending: {}'.format(ascending_digits))
print('Descending: {}'.format(descending_digits))
print('Reversed: {}'.format(reversed_digits))
