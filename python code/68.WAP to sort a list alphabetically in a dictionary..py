my_dict = { "fruits": ["apple", "orange", "banana"], "vegetables": ["carrot", 
"broccoli", "zucchini"], "animals": ["dog", "cat", "elephant", "bear"]} 
for key, value in my_dict.items(): 
    my_dict[key] = sorted(value) 
print(my_dict)
