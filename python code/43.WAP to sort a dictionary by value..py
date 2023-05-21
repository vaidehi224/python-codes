my_dict = {'apple': 30, 'banana': 50, 'cherry': 10, 'date': 20} 
sorted_dict_asc = dict(sorted(my_dict.items(), key=lambda x:x[1])) 
sorted_dict_desc = dict(sorted(my_dict.items(), key=lambda x:x[1], reverse=True)) 
print("Sorted dictionary in ascending order:", sorted_dict_asc) 
print("Sorted dictionary in descending order:", sorted_dict_desc)
