original_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 2} 
unique_dict = {} 
for key, value in original_dict.items(): 
     if value not in unique_dict.values(): 
         unique_dict[key] = value 
print(unique_dict)
