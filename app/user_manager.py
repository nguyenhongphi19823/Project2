# app/user_manager.py
import json
import logging
from typing import List, Dict, Any

logger = logging.getLogger(__name__)


class UserNotFoundError(Exception):
    """Raised when a user cannot be found by email."""
    def __init__(self, email: str):
        super().__init__(f"User with email {email} not found")
        self.email = email


class UserManager:
    def __init__(self, users: List[Dict[str, Any]]):
        # users là list các dict, ví dụ:
        # [{"email": "...", "role": "..."}, ...]
        self.users = users

    def get_user_by_email(self, email: str) -> Dict[str, Any]:
        for user in self.users:
            if user.get("email") == email:
                logger.info(f"User {email} found")
                return user

        logger.error(f"User {email} not found")
        raise UserNotFoundError(email)

    def add_user(self, email: str, role: str) -> None:
        logger.info(f"Adding user {email}")
        self.users.append({"email": email, "role": role})

    def remove_user_by_email(self, email: str) -> None:
        for user in self.users:
            if user.get("email") == email:
                logger.info(f"Removing user {email}")
                self.users.remove(user)
                return

        logger.error(f"User {email} not found for removal")
        raise UserNotFoundError(email)

    def save_to_file(self, filename: str) -> None:
        # Lưu users hiện tại ra file JSON (ghi đè)
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(self.users, file, indent=4)
        logger.info(f"Users saved to {filename}")


def load_users_from_file(filename: str) -> List[Dict[str, Any]]:
    """Load users list from a JSON file."""
    with open(filename, "r", encoding="utf-8") as file:
        data = json.load(file)

    # Validate nhẹ: JSON phải là list
    if not isinstance(data, list):
        raise ValueError("users.json must contain a JSON array (list of users)")
    return data