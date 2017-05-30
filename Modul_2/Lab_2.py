import random
import math
a = []
for i in range (5):
    a.append(random.randrange(0,100))


print(a)



print(random.random())

print(max(a))


print(math.factorial(max(a)))

# or

factorial = 5
qwerty = 1
for i in range(factorial):
    if i == 0:
        continue
    var1 = qwerty *(i+1)
    qwerty = var1
    print(qwerty)


