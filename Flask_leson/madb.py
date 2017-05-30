from typing import Tuple, List, Dict
import _string
import json


class MADBError(Exception):
    pass


class CredentialsError(MADBError):
    pass


class TableDoesNotExistError(MADBError):
    pass


class WrongTableKeysError(MADBError):
    pass


class RecordDoesNotExist(MADBError):
    pass


class DumpDBError(MADBError):
    pass


velues_har = False


# 1) should iterate through s
def validate_identifier(s):
    for c in s:
        if c not in ascii(s):
            return False
    return True


db = {
    'name': '',
    'file': '',
    'tables': {
    },
    'tables_meta': {
    },
    'db_users': [
    ],
}
user = {'username': '', 'password': ''}


# validate_identifier('Jack')

# """ Validates if `s` contains only ascii letters, numbes or underscore"""

# This function should
# 0) Validate if name, username and password are presented and contain only ascii letters or numbers
# 1) create file
# 2) write empty json db structure
# 3) create user
# 4) return Python data structure available for editing
def create_db(name: str, username: str, password: str):
    validation_result = True
    if len(name) > 0:
        if not validate_identifier(name):
            raise CredentialsError
        if not validate_identifier(username):
            raise CredentialsError
        if not validate_identifier(password):
            raise CredentialsError

    else:
        raise CredentialsError
    if validation_result:
        f = open('db_structure.json', 'w+')
        f.write(json.dumps(db))
        f.seek(0)
        data_base = json.loads(f.read())
        data_base['name'] = name
        db_users = data_base.get('db_users')
        user['username'] = username
        user['password'] = password
        db_users.append(user)
        f.seek(0)
        f.write(json.dumps(data_base))
        f.close()
        return data_base


"""
Initiates database with given name.
Adds database user with username and password.
"""


# your code goes here:


# This function should
# 1) open file
# 2) validate if provided username and password are valid
# 2.1) if validation failed, should `raise CredentialsError`
# 3) return Python data structure available for editing
def open_db(name: str, username: str, pasword: str):
    f = open(name, 'r')
    data_base = json.loads(f.read())
    users = data_base.get('db_users')
    for db_user in users:
        if db_user['username'] == username and db_user['password'] == pasword:
            return data_base
    raise CredentialsError


# """
# Opens database to work with.
# """

# your code goes here:


# This function should
# 1) Save current state of db to file.
def dump_db(db: Dict):
    try:
        f = open('db_dump.json', 'w')
        f.write(json.dumps(db))
        f.close()
    except:
        raise DumpDBError


def create_table(db: Dict, tablename: str, keys: List[str]):
    tables = db.get('tables_meta')
    tables[tablename] = {'keys': keys}
    tables[tablename]['size'] = len(keys)
    db['tables'][tablename] = []
    save_db(db)

    """
    Persists database to file system
    """


# This function should:
# 1) Check if table exists in db. If fails, should `raise TableDoesNotExistError`
# 2) Check if row_data keys match those specified in table_meta.
#    If fails, should `raise WrongTableKeysError`
# 3) Update table data in db: generate id, add dict to table data list.
# 4) Update table_meta in db: update size.
# 5) Return new db state
# Notes:
# `db` is dict of database structure, returned by open_db or create_db
def insert_row(db: Dict, table: str, row_data: Dict):
    table_exist = False
    for i in db.get('tables_meta'):
        if i == table:
            table_exist = True
            break
    if not table_exist:
        raise TableDoesNotExistError
    table_meta = db.get("tables_meta").get(table)
    table_keys = table_meta.get('keys')
    for key in row_data.keys():
        if key not in table_keys:
            raise WrongTableKeysError

    list_tables = db.get("tables").get(table)
    row_data['id'] = len(list_tables) + 1
    list_tables.append(row_data)
    table_meta['size'] = len(list_tables)
    save_db(db)


"""
    Inserts row with `row_data` into `table` of `db`
    """


# This function should:
# 1) Check if table exists in db. If fails, should `raise TableDoesNotExistError`
# 2) Check if row_update_data keys are in those specified in table_meta.
#    If fails, should `raise WrongTableKeysError`
# 3) Find row by id. If fails, should `raise RecordDoesNotExist`
# 4) Update data in that row with new given values.
# 5) Return new db state
# Notes:
# `db` is dict of database structure, returned by open_db or create_db
def update_row_by_id(db: Dict, table: str, id: int, row_update_data: Dict):
    table_exist = False
    for i in db.get('tables_meta'):
        if i == table:
            table_exist = True
            break
    if not table_exist:
        raise TableDoesNotExistError
    row_keys = db.get('tables_meta')
    row_keys_set = set(row_keys)
    row_update_data_set = set(row_update_data)
    flag = row_update_data_set.isdisjoint(row_keys_set)
    if not flag:
        raise WrongTableKeysError
    chek_id = db.get("tables").get(table)
    for dictionary in chek_id:
        if dictionary['id'] == id:
            dictionary.update(row_update_data)
            save_db(db)
            return db
    raise RecordDoesNotExist


"""
   Updates row by id with row_update_data
"""


# This function should:
# 1) Check if table exists in db. If fails, should `raise TableDoesNotExistError`
# 2) Check if row_update_data keys are in those specified in table_meta.
#    If fails, should `raise WrongTableKeysError`
# 3) Find row by id. If fails, should `raise RecordDoesNotExist`
# 4) Delete row from table data
# 5) Update table_meta.
# 6) Return new db state
# Notes:
# `db` is dict of database structure, returned by open_db or create_db
def delete_row_by_id(db: Dict, table: str, id: int):
    table_exist = False
    for i in db.get('tables_meta'):
        if i == table:
            table_exist = True
            break
    if not table_exist:
        raise TableDoesNotExistError
    chek_id = db.get("tables").get(table)
    for dictionary in chek_id:
        if dictionary['id'] != id:
            dictionary.clear()
            save_db(db)
    return db



"""
    Deletes row by id
"""


def save_db(database: Dict):
    f = open('db_structure.json', 'w')
    f.write(json.dumps(database))
    f.close()
