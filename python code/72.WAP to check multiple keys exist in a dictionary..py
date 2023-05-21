my_dict = {'apple': 5, 'banana': 3, 'orange': 2, 'pear': 1} 
keys_to_check = ['apple', 'banana', 'mango'] 
for key in keys_to_check: 
    if key in my_dict: 
        print(key, 'exists in the dictionary') 
    else: 
        print(key, 'does not exist in the dictionary')
