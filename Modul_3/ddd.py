import os


def get_extension(filename):
    return os.path.splitext(filename)[1]


def check_ext(filename, new_filename):
    if get_extension(filename) != get_extension(new_filename):
        is_overwrite = input('Extensions do not match. Proceed? (y/n) ')
        if is_overwrite.lower() == 'n':
            return False
    return True


def check_file_exists(filename):
    if os.path.isfile(filename):
        is_overwrite = input('File "{0}" exists. Proceed? (y/n)'.format(filename))
        if is_overwrite.lower() == 'n':
            return False
    return True


def real_copy(filename, new_filename):
    with open(filename, 'r', encoding='utf-8') as input_file:
        data = input_file.read()

        with open(new_filename, 'w', encoding='utf-8') as output_file:
            output_file.write(data)


def copy(filename, new_filename):
    extensions_match = check_ext(filename, new_filename)
    write_file = check_file_exists(new_filename)
    if extensions_match and write_file:
        real_copy(filename, new_filename)
    else:
        return

copy('homework.py', 'new_home')
