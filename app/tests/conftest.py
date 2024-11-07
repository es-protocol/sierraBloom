import pytest
from app.app import create_app

@pytest.fixtures
def client():
    app = create_app()
    with app.app_context():
        yield app.test_client()