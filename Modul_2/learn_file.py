import json
f = open('somefile.json', 'r')
load_answer = f.read()
print(load_answer)
print(type(load_answer))
var1 = json.loads(load_answer)
print(var1)
print(type(var1))

result = 0
for i in var1:
    print(i.get("question"))
    use_run = input('\n')
    use_run2 = str(use_run)
    if use_run2.lower().strip() == i['answer'].lower():
        print('true')
        result+=1
    else:
        print('false')
print('Result true', result, 'is', len(var1))

f.close()


