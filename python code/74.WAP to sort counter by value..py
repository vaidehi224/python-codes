from collections import Counter 
my_counter = Counter( {'Math': 81, 'Physics':83,'Chemistry': 87}) 
sorted_counter = sorted(my_counter.items(), key=lambda x: x[1], reverse=True) 
print(sorted_counter)
