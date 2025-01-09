from .user_repository import UserRepository
from src.models.settings.db_connection_handler import db_connection_handler

def test_repository():
    db_connection_handler.connect()
    conn = db_connection_handler.get_connection()
    repo = UserRepository(conn)

    username = "johndoe"
    password = "123456"

    user = repo.get_user_by_username(username)
    print()
    print(user)
