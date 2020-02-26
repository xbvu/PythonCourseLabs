def list_function(number, lst):
    average = sum(lst) / len(lst)
    min_value = min(lst)
    max_value = max(lst)
    less_count = len([i for i in lst if i < number])
    more_count = len([i for i in lst if i > number])
    return average, min_value, max_value, less_count, more_count

# testing
print(list_function(5, [4,8,2,10,3,6]))
