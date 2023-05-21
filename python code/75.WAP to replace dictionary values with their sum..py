d = {'a': 1, 'b': 2, 'c': 3}
sum_values = sum(d.values())
d = {key: sum_values for key in d.keys()}
print(d)
