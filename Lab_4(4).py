sort_me = { 
    "a": [7, 1, 9], 
    "b": [8, -4, 3],
    "c": [9, 10, 151],
    "d": [-3, 9, 11]
}
    
list_output = sorted(sort_me.items(), key=lambda sort_me: sort_me[1][1])
dict_output = {}

for list_item in list_output:
    dict_output[list_item[0]] = list_item[1]
print(list_output)
print(dict_output)
