import pytest
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from .login_creator_view import LoginCreatorView

class MockController:
    def create(self, username, password):
        return {"token": "abcd1234"}

def test_handle_login_creator():
    body = {
        "username": "johndoe",
        "password": "123456"
    }
    request = HttpRequest(body=body)

    mock_controller = MockController()
    login_creator_view = LoginCreatorView(mock_controller)

    response = login_creator_view.handle(request)

    assert isinstance(response, HttpResponse)
    assert response.body == {'data': {'token': 'abcd1234'}}
    assert response.status_code == 200

def test_handle_login_creator_with_validation_error():
    body = {
        "password": "123456"
    }
    request = HttpRequest(body=body)

    mock_controller = MockController()
    login_creator_view = LoginCreatorView(mock_controller)

    with pytest.raises(Exception) as excinfo:
        login_creator_view.handle(request)
    
    assert str(excinfo.value) == "Invalid input"

def test_handle_login_creator_with_invalid_types():
    body = {
        "username": 12345,
        "password": None
    }
    request = HttpRequest(body=body)

    mock_controller = MockController()
    login_creator_view = LoginCreatorView(mock_controller)

    with pytest.raises(Exception) as excinfo:
        login_creator_view.handle(request)
    
    assert str(excinfo.value) == "Invalid input"
