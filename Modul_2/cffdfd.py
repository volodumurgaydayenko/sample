import json
f = open('test-data.json','w')

array = '{"fruits": ["apple", "banana", "orange"]}'
data  = json.loads(array)


f.close()








