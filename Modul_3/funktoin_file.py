import os


def copy(filename, newfilename):
    name, file_extension = os.path.splitext(filename)
    name, file_extension2 = os.path.splitext(newfilename)
    if file_extension != file_extension2:
        print('Warning! File extensions do not match!')
        print('you want destroy kopy, y/n')
        chek_var = input('y/n ')
        if chek_var == 'y':
            return
    else:
        f = open(filename, 'r')
        some_text = f.read()
        f.close()
        if os.path.isfile(newfilename):
            is_overwrite = input('File "{0}" exists. Proceed? (y/n)'.format(newfilename))
        if is_overwrite.lower() == 'n':
            return False
        else:
            f = open(newfilename, 'w')
            f.write(some_text)
            f.close()


copy('file.txt', 'file2.txt')
