# def create_person_account(first_name, last_name, age, gender=None, phone=None, city='London', country='GB'):
#     dictionary = {
#         'first_name': first_name,
#         'last_name': last_name,
#         'age': age,
#         'gender': gender,
#         'phone': phone,
#         'city': city,
#         'country': country
#     }
#     if phone is None:
#         del dictionary['phone']
#     return dictionary
#
#
# assert create_person_account('John', 'Newman', 12, 'M', '123', 'Kyiv', 'Ukraine') == {
#     'first_name': 'John',
#     'last_name': 'Newman',
#     'age': 12,
#     'gender': 'M',
#     'phone': '123',
#     'city': 'Kyiv',
#     'country': 'Ukraine',
# }
#
#
# def create_person_account2(first_name, last_name, age, gender, phone, city, country, **kwargs):
#     dictionary = {
#         'first_name': first_name,
#         'last_name': last_name,
#         'age': age,
#         'gender': gender,
#         'phone': phone,
#         'city': city,
#         'country': country
#     }
#     return dictionary
#
#
# def var_dic_call(arg1, arg2, arg3, arg4):
#     # print ("arg1:", arg1)
#     # print ("arg2:", arg2)
#     # print ("arg3:", arg3)
#     # print ("arg3:", arg4)
#     for keys, value in var_dic.items():
#         print(keys, value)
#
#
# var_dic = {"arg3": 3, "arg2": "two", "arg4": "fo"}
# var_dic_call(1, **var_dic)
#
#
# def create_person_account2(first_name, last_name, age, city='London', country='GB', **kwargs):
#     dictionary = {
#         'first_name': first_name,
#         'last_name': last_name,
#         'age': age,
#         'city': city,
#         'country': country,
#         'children': ['Bonnie', 'Clyde']
#     }
#     return dictionary
#
#
# assert create_person_account2('John', 'Newman', 22, children=['Bonnie', 'Clyde']) == {
#     'first_name': 'John',
#     'last_name': 'Newman',
#     'age': 22,
#     'city': 'London',
#     'country': 'GB',
#     'children': ['Bonnie', 'Clyde'],
# }
#
# xs = [1, 3, 5, 7]
#
# # def sum_v(xs, s=0):
# #     print(xs, s)
# #     if xs:
# #         sum_v(xs[1:], s + xs[0])
# #     else:
# #         print(s)
# #
# #
# # sum_v(xs)
#
# xs2 = [
#     {'name': 'Jon', 'age': 13},
#     {'name': 'Bob', 'age': 20},
#     {'name': 'Lor', 'age': 28}
#
# ]


# def sorted2 (xs2, key=lambda el: el['age']):
#     print(xs2)

# sorted2(xs2)
#
# def apply(func, *args, **kwargs):
#     print(*args)
#     print(**kwargs)
#     print(func)
#     return apply(*args, **kwargs)
#
#
# apply(lambda a, b: a + b, 2, 5)


# def max2(a, b):
#     if a > b:
#         return a
#     else:
#         return b
#
#
# max2(2, 3)

#
# def sum23(x, y):
#     return x + y
#
#
# def perform_operation(func, a, b):
#     return print(func(a, b))
#
#     def sum23(x, y):
#         return x + y
#
#     sum23(5, 10)
#
#
# perform_operation(sum23, 2, 3)


# def faktory_profile(gender):
#     def create_profile(**kwargs):
#         kwargs['gender'] = gender
#         return kwargs
#
#
# faktory_profile('Male')
# faktory_profile('Famele')
# create_male = faktory_profile('Male')
# create_profile = faktory_profile('Famele')
#
# create_profile({'age': 30})

