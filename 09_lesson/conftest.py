import pytest
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
import requests


class UserTable:
    def __init__(self, connection_string):
        self.engine = create_engine(connection_string)

    def get_users(self):
        try:
            with self.engine.connect() as conn:
                result = conn.execute(text("SELECT user_id, subject_id, user_email FROM users"))
                return [dict(row._mapping) for row in result]
        except SQLAlchemyError as e:
            print(f"Database error in get_users: {e}")
            return []

    def create_user(self, user_email, subject_id):
        try:
            with self.engine.connect() as conn:
                result = conn.execute(
                    text(
                        "INSERT INTO users (user_email, subject_id) VALUES (:user_email, :subject_id) RETURNING user_id"),
                    {"user_email": user_email, "subject_id": subject_id}
                )
                conn.commit()
                return result.scalar()
        except SQLAlchemyError as e:
            print(f"Database error in create_user: {e}")
            return None

    def delete_user(self, user_id):
        try:
            with self.engine.connect() as conn:
                conn.execute(text("DELETE FROM users WHERE user_id = :user_id"), {"user_id": user_id})
                conn.commit()
                return True
        except SQLAlchemyError as e:
            print(f"Database error in delete_user: {e}")
            return False

    def update_user(self, user_id, user_email=None, subject_id=None):
        try:
            with self.engine.connect() as conn:
                query = "UPDATE users SET "
                params = {"user_id": user_id}
                updates = []

                if user_email:
                    updates.append("user_email = :user_email")
                    params["user_email"] = user_email
                if subject_id is not None:
                    updates.append("subject_id = :subject_id")
                    params["subject_id"] = subject_id

                if updates:
                    query += ", ".join(updates) + " WHERE user_id = :user_id"
                    conn.execute(text(query), params)
                    conn.commit()
                    return True
                return False
        except SQLAlchemyError as e:
            print(f"Database error in update_user: {e}")
            return False

    def get_user_by_id(self, user_id):
        try:
            with self.engine.connect() as conn:
                result = conn.execute(
                    text("SELECT user_id, subject_id, user_email FROM users WHERE user_id = :user_id"),
                    {"user_id": user_id}
                )
                return [dict(row._mapping) for row in result]
        except SQLAlchemyError as e:
            print(f"Database error in get_user_by_id: {e}")
            return []

    def get_max_id(self):
        try:
            with self.engine.connect() as conn:
                result = conn.execute(text("SELECT MAX(user_id) as max_id FROM users"))
                return result.scalar()
        except SQLAlchemyError as e:
            print(f"Database error in get_max_id: {e}")
            return None


@pytest.fixture(scope="session")
def db():
    connection_string = "postgresql://postgres:671@localhost:5432/qa1"
    return UserTable(connection_string)


@pytest.fixture
def cleanup(db):
    """Фикстура для очистки тестовых данных"""
    test_users = []
    yield test_users
    # Очистка после каждого теста
    for user_id in test_users:
        db.delete_user(user_id)
