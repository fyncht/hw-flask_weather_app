from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    balance = db.Column(db.Float, nullable=False)

    def __init__(self, username, balance):
        self.username = username
        self.balance = balance

    def update_balance(self, amount):
        self.balance = max(0, self.balance + amount)  # предотвращаем отрицательный баланс
        db.session.commit()

    @classmethod
    def add_user(cls, username, balance):
        new_user = cls(username=username, balance=balance)
        try:
            db.session.add(new_user)
            db.session.commit()
            return new_user
        except IntegrityError:
            db.session.rollback()
            print("Пользователь с таким именем уже существует.")
            return None

    @classmethod
    def find_by_id(cls, user_id):
        return cls.query.get(user_id)

    def delete_user(self):
        db.session.delete(self)
        db.session.commit()


# def update_balance(self, amount):
#     try:
#         if self.balance + amount < 0:
#             raise ValueError("Нельзя установить отрицательный баланс.")
#         self.balance += amount
#         db.session.commit()
#     except Exception as e:
#         db.session.rollback()
#         print(f"Произошла ошибка при обновлении баланса: {e}")