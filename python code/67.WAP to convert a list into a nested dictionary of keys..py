keys = ['a', 'b', 'c', 'd']
nested_dict = {}
current_dict = nested_dict
for key in keys[:-1]:
    current_dict[key] = {}
    current_dict = current_dict[key]
    current_dict[keys[-1]] = 'value'
print(nested_dict)
