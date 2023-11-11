from flask import Flask, jsonify, request
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'DB_HOST'
app.config['MYSQL_USER'] = 'DB_USERNAME'
app.config['MYSQL_PASSWORD'] = 'DB_PASSWORD'
app.config['MYSQL_DB'] = 'DB_NAME'
mysql = MySQL(app)


@app.route('/data', methods=['POST'])
def add_data():
    cur = mysql.connection.cursor()
    email = request.json['email']
    password = request.json['password']
    name = request.json['name']
    deliverer = request.json['deliverer']
    cur.execute('''INSERT INTO Users (Email, Password, Name, Deliverer) VALUES (%s, %s, %s, %s)''',
                (email, password, name, deliverer))
    mysql.connection.commit()
    cur.close()
    return jsonify({'message': 'Data added successfully'})


if __name__ == '__main__':
    app.run()
