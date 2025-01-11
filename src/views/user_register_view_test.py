import pytest
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from .user_register_view import UserRegisterView

class MockController:
    def registry(self, username, password):
        return { "test": "test" }

def test_handle_user_register():
    body = {
        "username": "johndoe",
        "password": "123456"
    }
    request = HttpRequest(body=body)

    mock_controller = MockController()
    user_register_view = UserRegisterView(mock_controller)

    response = user_register_view.handle(request)

    assert isinstance(response, HttpResponse)
    assert response.body == {'data': {'test': 'test'}}
    assert response.status_code == 201

def test_handle_user_register_with_validation_error():
    body = {
        "password": "123456"
    }
    request = HttpRequest(body=body)

    mock_controller = MockController()
    user_register_view = UserRegisterView(mock_controller)

    with pytest.raises(Exception):
        user_register_view.handle(request)