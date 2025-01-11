from src.models.interfaces.user_repository import UserRepositoryInterface
from .interfaces.balance_editor import BalanceEditorInterface

class BalanceEditor(BalanceEditorInterface):
    def __init__(self, user_repository: UserRepositoryInterface) -> None:
        self.__user_repository = user_repository

    def edit(self, user_id: int, new_balance: float) -> dict:
        self.__find_user(user_id)
        self.__user_repository.edit_balance(user_id, new_balance)
        return self.__format_response(user_id, new_balance)

    def __find_user(self, user_id: int) -> dict:
        user = self.__user_repository.get_user_by_id(user_id)
        if not user:
            raise Exception("User not found")
        return user
    
    def __format_response(self, user_id: int, new_balance: float) -> dict:
        return {
            "type": "User",
            "user_id": user_id,
            "new_balance": new_balance,
        }