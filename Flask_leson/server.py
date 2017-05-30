from flask import Flask, jsonify, request
from Flask_leson.madb import *
from Modul_4.madb import *

app = Flask(__name__)


@app.route('/db/get', methods=['GET'])
def get_db():
    return jsonify(db)


@app.route('/db/create_table', methods=['POST'])
def insert_table():
    table_name = request.json['tableName']
    columns = request.json['columns']
    create_table(db, table_name, columns)
    return jsonify(db)


@app.route('/db/create_row', methods=['POST'])
def insert_table_row():
    table_name = request.json['tableName']
    columns = request.json['columns']
    insert_row(db, table_name, columns)
    return jsonify(db)


@app.route('/db/create_row_by_id', methods=['POST'])
def insert_table_row_by_id():
    table_name = request.json['tableName']
    id_name = request.json['id']
    columns = request.json['columns']
    update_row_by_id(db, table_name, id_name, columns)
    return jsonify(db)


@app.route('/db/create_row_by_id_delete', methods=['POST'])
def insert_table_row_by_id_delete():
    table_name = request.json['tableName']
    id_name = request.json['id']
    delete_row_by_id(db, table_name, id_name)
    return jsonify(db)


if __name__ == '__main__':
    db = create_db('server_db', 'Vova', 'q1q2w3r4')
    app.run(debug=False)
