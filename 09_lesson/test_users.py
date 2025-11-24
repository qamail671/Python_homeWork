import pytest
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, select, insert, update, delete
from sqlalchemy.orm import sessionmaker

# Подключение к базе данных через SQLAlchemy с использованием psycopg2-binary
DATABASE_URL = "postgresql+psycopg2://postgres:671@localhost:5432/qa1"

engine = create_engine(DATABASE_URL)
metadata = MetaData()

# Описание таблицы users
users = Table(
    "users", metadata,
    Column("user_id", Integer, primary_key=True),
    Column("subject_id", Integer, nullable=False),
    Column("user_email", String, nullable=False)
)

Session = sessionmaker(bind=engine)


@pytest.fixture
def session():
    """Фикстура для создания и закрытия сессии с базой данных."""
    session = Session()
    yield session
    session.close()


def test_add_user(session):
    # Добавление нового пользователя
    ins = insert(users).values(user_id=9999, subject_id=101, user_email="test_add@example.com")
    session.execute(ins)
    session.commit()

    # Проверка, что пользователь добавлен
    sel = select(users).where(users.c.user_id == 9999)
    result = session.execute(sel).fetchone()
    assert result is not None
    assert result.user_email == "test_add@example.com"

    # Удаляем добавленного пользователя для чистоты теста
    del_stmt = delete(users).where(users.c.user_id == 9999)
    session.execute(del_stmt)
    session.commit()


def test_update_user_email(session):
    # Вставляем пользователя для обновления
    ins = insert(users).values(user_id=8888, subject_id=102, user_email="old_email@example.com")
    session.execute(ins)
    session.commit()

    # Обновляем email пользователя
    upd = update(users).where(users.c.user_id == 8888).values(user_email="new_email@example.com")
    session.execute(upd)
    session.commit()

    # Проверяем обновление
    sel = select(users).where(users.c.user_id == 8888)
    result = session.execute(sel).fetchone()
    assert result.user_email == "new_email@example.com"

    # Удаляем тестового пользователя
    del_stmt = delete(users).where(users.c.user_id == 8888)
    session.execute(del_stmt)
    session.commit()


def test_delete_user(session):
    # Добавляем пользователя для удаления
    ins = insert(users).values(user_id=7777, subject_id=103, user_email="delete_me@example.com")
    session.execute(ins)
    session.commit()

    # Удаляем пользователя
    del_stmt = delete(users).where(users.c.user_id == 7777)
    result = session.execute(del_stmt)
    session.commit()

    # Проверяем, что пользователя нет
    sel = select(users).where(users.c.user_id == 7777)
    result = session.execute(sel).fetchone()
    assert result is None
