import pytest
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from .balance_editor_view import BalanceEditorView

class MockController:
    def edit(self, user_id, new_balance):
        return {"status": "success", "updated_balance": new_balance}

def test_handle_balance_editor():
    body = {
        "new_balance": 500.75
    }
    param = {
        "user_id": "12345"
    }
    request = HttpRequest(body=body, params=param)

    mock_controller = MockController()
    balance_editor_view = BalanceEditorView(mock_controller)

    response = balance_editor_view.handle(request)

    assert isinstance(response, HttpResponse)
    assert response.body == {"data": {"status": "success", "updated_balance": 500.75}}
    assert response.status_code == 200

def test_handle_balance_editor_with_missing_body():
    body = {}
    param = {
        "user_id": "12345"
    }
    request = HttpRequest(body=body, params=param)

    mock_controller = MockController()
    balance_editor_view = BalanceEditorView(mock_controller)

    with pytest.raises(Exception) as excinfo:
        balance_editor_view.handle(request)
    
    assert str(excinfo.value) == "Invalid input"

def test_handle_balance_editor_with_missing_param():
    body = {
        "new_balance": 500.75
    }
    param = {}
    request = HttpRequest(body=body, params=param)

    mock_controller = MockController()
    balance_editor_view = BalanceEditorView(mock_controller)

    with pytest.raises(Exception) as excinfo:
        balance_editor_view.handle(request)
    
    assert str(excinfo.value) == "Invalid input"

def test_handle_balance_editor_with_invalid_balance_type():
    body = {
        "new_balance": "500.75"
    }
    param = {
        "user_id": "12345"
    }
    request = HttpRequest(body=body, params=param)

    mock_controller = MockController()
    balance_editor_view = BalanceEditorView(mock_controller)

    with pytest.raises(Exception) as excinfo:
        balance_editor_view.handle(request)
    
    assert str(excinfo.value) == "Invalid input"
