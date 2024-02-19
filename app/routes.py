from flask import Blueprint, request, jsonify
from .models import User, db
from .weather import fetch_weather

bp = Blueprint('routes', __name__)

from flask import render_template


@bp.route('/')
def home():
    return render_template('index.html')


@bp.route('/update_balance', methods=['GET'])
def update_balance():
    user_id = request.args.get('user_id')  # извлекаем 'user_id' из параметров запроса
    city = request.args.get('city')  # извлекаем 'city' из параметров запроса
    other_city = request.args.get('otherCity')

    # если выбран "Другой", используем значение из поля ввода
    if city == 'Other':
        city = other_city

    if not user_id or not city:
        # если 'user_id' или 'city' не предоставлены, возвращаем сообщение об ошибке
        return jsonify({'error': 'Missing required parameters'}), 400

    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    temperature = fetch_weather(city)
    if temperature is None:
        return jsonify({'error': 'Failed to fetch weather data'}), 500

    user.update_balance(temperature)

    # возвращаем шаблон с результатами
    return render_template('result.html', username=user.username, balance=user.balance)






# OLD
# @bp.route('/update_balance/<int:user_id>/<city>', methods=['GET'])
# def update_balance(user_id, city):
#     user = User.query.get(user_id)
#     if not user:
#         return jsonify({'error': 'User not found'}), 404
#
#     temperature = fetch_weather(city)
#     if temperature is None:
#         return jsonify({'error': 'Failed to fetch weather data'}), 500
#
#     user.update_balance(temperature)
#     return jsonify({'username': user.username, 'new_balance': user.balance})
