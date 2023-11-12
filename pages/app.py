from flask import Flask, jsonify, request, app
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
from datetime import datetime
from sqlalchemy import ForeignKey
import pymysql

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://HackPrincetonUser:HackPrinceton@LAPTOP-JCH0P14A/hackprinceton'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app, resources={r"/*": {"origins": "*"}})
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class User(db.Model):
    __tablename__ = 'Users'
    User_ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(120), nullable=True)
    deliverer = db.Column(db.Boolean, nullable=False)


@app.route('/test-database-connection')
def test_database_connection():
    try:
        result = User.query.first()
        if result:
            return jsonify({
                'message': 'Database connection successful',
                'result': {
                    'User_ID': result.User_ID,  # Corrected attribute name
                    'email': result.email,
                    'password': result.password,
                    'name': result.name,
                    'deliverer': result.deliverer
                }
            })
        else:
            return jsonify({'message': 'No users found in the database'})
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'error': str(e)})


@app.route('/data', methods=['POST'])
def add_data():
    try:
        data = request.json
        new_user = User(User_ID=None, email=data['email'], password=data['password'], name=data.get('name'),
                        deliverer=data['deliverer'])
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'Data added successfully'})
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'error': str(e)})


class Order(db.Model):
    __tablename__ = 'Orders'
    Order_ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    order_date = db.Column(db.DateTime, nullable=False)
    location = db.Column(db.String(255), nullable=False)
    product = db.Column(db.String(255), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)


@app.route('/order_data', methods=['POST'])
def add_order_data():
    try:
        order_data = request.json
        order_data_str = order_data['order_date'].strip('\"')
        order_date = datetime.strptime(order_data_str, '%Y-%m-%d %H:%M:%S')

        new_order = Order(Order_ID=None, order_date=order_date, location=order_data['location'],
                          product=order_data['product'], quantity=order_data['quantity'])
        db.session.add(new_order)
        db.session.commit()
        return jsonify({'message': 'Data added successfully'})
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'error': str(e)})


class Deliver(db.Model):
    __tablename__ = 'Deliveries'
    Delivery_ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Order_ID = db.Column(db.Integer, nullable=False)
    completed_date = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(255), nullable=False)


@app.route('/delivery_data', methods=['POST'])
def add_delivery_data():
    try:
        delivery_data = request.json
        delivery_data_str = delivery_data['completed_date'].strip('\"')
        completed_date = datetime.strptime(delivery_data_str, '%Y-%m-%d %H:%M:%S')
        order_id = delivery_data['Order_ID']
        complete_delivery = Deliver(Delivery_ID=None, Order_ID=order_id, completed_date=completed_date,
                                    status=delivery_data['status'])
        db.session.add(complete_delivery)
        db.session.commit()
        return jsonify({'message': 'Data added successfully'})
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'error': str(e)})


@app.route('/order_data', methods=['GET'])
def get_all_order_data():
    try:
        orders = Order.query.all()
        order_list = []
        for order in orders:
            order_data = {
                'Order_ID': order.Order_ID,
                'order_date': order.order_date.strftime('%Y-%m-%d %H:%M:%S'),
                'location': order.location,
                'product': order.product,
                'quantity': order.quantity
            }
            order_list.append(order_data)

        return jsonify(order_list)
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'error': str(e)})


@app.route('/delivery_data', methods=['GET'])
def get_all_delivery_data():
    try:
        deliveries = Deliver.query.all()
        delivery_list = []
        for delivery in deliveries:
            delivery_data = {
                'completed_date': delivery.completed_date.strftime('%Y-%m-%d %H:%M:%S'),
                'status': delivery.status,
                'Order_ID': delivery.Order_ID,
                'Delivery_ID': delivery.Delivery_ID
            }
            delivery_list.append(delivery_data)

        return jsonify(delivery_list)
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'error': str(e)})


if __name__ != '__main__':
    pass
else:
    with app.app_context():
        db.create_all()
        migrate.init_app(app, db)
    app.run(host='0.0.0.0', port=5000)
