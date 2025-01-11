from src.controllers.balance_editor import BalanceEditor

class MockUserRepository:
    def __init__(self) -> None:
        self.users = {}
        self.edited_user = None

    def get_user_by_id(self, user_id: int) -> dict:
        return self.users.get(user_id)

    def edit_balance(self, user_id: int, new_balance: float) -> None:
        if user_id in self.users:
            self.users[user_id]['balance'] = new_balance
            self.edited_user = self.users[user_id]

def test_edit_balance():
    repository = MockUserRepository()
    controller = BalanceEditor(repository)

    user_id = 1
    initial_balance = 100
    new_balance = 200

    repository.users[user_id] = {"id": user_id, "balance": initial_balance}

    response = controller.edit(user_id, new_balance)

    assert response["type"] == "User"
    assert response["user_id"] == user_id
    assert response["new_balance"] == new_balance

    assert repository.edited_user is not None
    assert repository.edited_user["balance"] == new_balance
