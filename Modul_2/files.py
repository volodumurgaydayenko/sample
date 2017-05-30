import json

xs = [1, 2, 3, 4, {'mode': True}]
dumped = json.dumps(xs)
print(type(dumped))
print(dumped)
f = open('test-data.json', 'w')
f.write(dumped)
f.close()

f = open('test-data.json', 'r+')
readData = f.read()
load = json.loads(readData)
load.append("1231")
print(type(f))
print(load)







# f = open('stats.json', 'w')
# stats_json = json.dumps(xs)
# f.write(stats_json)
# f.close()
#
# with open('stats.json', 'w') as stats_file:
#     stats_json = json.dumps(xs)
#     stats_file.write(stats_json)
