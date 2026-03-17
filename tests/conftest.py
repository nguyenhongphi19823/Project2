import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pytest
from app.user_manager import UserManager
from app.user_manager import load_users_from_file
@pytest.fixture
def manager():

    users = load_users_from_file("app/users.json")

    return UserManager(users)