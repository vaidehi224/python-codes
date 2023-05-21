data = {' first name ': ' John', ' last name ': ' Smith ', ' age ': 25}
new_data = {}
for key, value in data.items():
    new_key = key.strip()
    new_data[new_key] = value
print(new_data)
