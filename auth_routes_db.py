# auth_routes_db.py – versi SQLAlchemy untuk auth
from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User
import jwt, datetime

auth = Blueprint('auth', __name__)
SECRET_KEY = "your_secret_key"

@auth.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    role = data.get('role', 'user')

    if User.query.filter_by(username=username).first():
        return jsonify({'error': 'User already exists'}), 400

    hashed = generate_password_hash(password)
    new_user = User(username=username, password=hashed, role=role)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User registered'})

@auth.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()
    if not user or not check_password_hash(user.password, password):
        return jsonify({'error': 'Invalid credentials'}), 401

    token = jwt.encode({
        'username': user.username,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)
    }, SECRET_KEY, algorithm='HS256')

    return jsonify({'token': token, 'role': user.role, 'plan': user.plan})

@auth.route('/verify', methods=['GET'])
def verify():
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({'error': 'Token missing'}), 403
    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        user = User.query.filter_by(username=decoded['username']).first()
        if not user:
            return jsonify({'error': 'User not found'}), 404
        return jsonify({'username': user.username, 'role': user.role, 'plan': user.plan})
    except Exception as e:
        return jsonify({'error': str(e)}), 401
