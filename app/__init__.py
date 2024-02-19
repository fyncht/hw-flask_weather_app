from flask import Flask
from .models import db, User
from .routes import bp


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    app.register_blueprint(bp)

    with app.app_context():
        db.create_all()
        if User.query.count() == 0:
            # заполнение базы данных начальными данными
            initial_users = [User(username=f'User{i}', balance=5000 + 2000 * i) for i in range(1, 6)]
            db.session.bulk_save_objects(initial_users)
            db.session.commit()

    return app
