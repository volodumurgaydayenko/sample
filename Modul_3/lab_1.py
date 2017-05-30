import os


# def max_int(a, b):
#     if isinstance(a,(int, float)) and isinstance(b,(int, float)):
#         if a > b:
#             return print(a)
#         elif b > a:
#             return print(b)
#         else:
#             return print(a)
#     else:
#         return print('Exeption')
#
#
# max_int('vrvr', 5)
#
#
#
# def sum2(xs):
#     result = 0
#
#     for i in xs:
#         if isinstance(i, (int, float)):
#             result = result + i
#         else:
#             result = 'dgt'
#             break
#     return print(result)
#
#
# sum2([-3, 'cgcg', 2])
#
# def sum2(xs):
#     result = 0
#
#     for i in xs:
#         if isinstance(i, (int, float)):
#             result = result + i
#         else:
#             result = 'dgt'
#             break
#     return print(result)
#
#
# sum2([1, 2, 3])
#
# def sum2(s: str, letter: str):
#     if isinstance(s, (str)) and isinstance(letter,(str)):
#         return print(' ')
#
#
# sum2('aaa', 'a')




# def sum2(s:str, letter: str):
#     if isinstance(s, (str)) and isinstance(letter,(str)):
#         if len(s) > len(letter):
#             return print(s)
#         else:
#             return print(letter)
#
# sum2('bbb', 'a')
#
#
#
# def sum2(s: str, letter: str):
#     result = []
#     if isinstance(s, (str)) and isinstance(letter, (str)):
#         for i in s:
#             if i.isupper():
#                 result.append(i)
#                 ''.join(result)
#         return print(''.join(result))
#
#
# sum2('AaAa', 'a')








# def sum2(s: str, letter: str):
#     result = []
#
#     if isinstance(s, (str)) and isinstance(letter, (str)):
#         for i in s:
#             if i != letter:
#                 result.append(i)
#     s = ''.join(result)
#     print(s)
#
#
# sum2('averge', 'a')

# def get_extension(filename):
# f = open(filename, 'w')
# name, file_extension = os.path.splitext(filename)
# f.close()
# return file_extension.replace('.', '')


# assert get_extension('file.png') == 'png'
# assert get_extension('file.jpeg') == 'jpeg'
# assert get_extension('file') == ''
# assert get_extension('prefix.file.png') == 'png'
# assert get_extension('') == ''


# def copy(filename, newfilename):
#     f = open(filename, 'w')
#     some_string = 'Hello'
#     f.write(some_string)
#     name, file_extension = os.path.splitext(filename)
#     f.close()
#
#     f = open(newfilename, 'w')
#     some_string2 = ''
#     f.write(some_string2)
#     name2, file_extension2 = os.path.splitext(newfilename)
#     if file_extension != file_extension2:
#         print('Warning! File extensions do not match!')
#     else:
#         write_file = f.write(some_string)
#         f.close()
#         return
#
#
# copy('files.txt', 'file2.txt')
def chek_ext (filename):
    pass
def chek_file_ex (newfilename):
    pass

def copy(filename, newfilename):
    if chek_ext (filename, newfilename) and chek_file_ex (newfilename):
        f = open(filename, 'r')
        
    some_string = 'Hello'
    f.write(some_string)
    name, file_extension = os.path.splitext(filename)
    f.close()

    f = open(newfilename, 'w')
    some_string2 = ''
    f.write(some_string2)
    name2, file_extension2 = os.path.splitext(newfilename)
    if file_extension != file_extension2:
        print('Warning! File extensions do not match!')
    else:
        write_file = f.write(some_string)
        f.close()
        return


copy('files.txt', 'file2.txt')
