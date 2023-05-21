dict1 = {'key1': 1, 'key2': 3, 'key3': 2} 
dict2 = {'key1': 1, 'key2': 2} 
for key, value in dict1.items(): 
    if key in dict2 and value == dict2[key]: 
        print(f"{key}: {value} is present in both dict1 and dict2")
