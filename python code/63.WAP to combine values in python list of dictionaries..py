data = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, 
{'item': 'item1', 'amount': 750}]
result = {}
for item in data:
    if item['item'] not in result:
        result[item['item']] = item['amount']
    else:
        result[item['item']] += item['amount']
print(result)
