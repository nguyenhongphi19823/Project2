from app.user_manager import UserManager, UserNotFoundError
from app.user_manager import load_users_from_file
users = load_users_from_file("app/users.json")