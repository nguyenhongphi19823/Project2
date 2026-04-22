# app/user_manager.py

import json  # Thư viện built-in của Python dùng để đọc (load) và ghi (dump) dữ liệu JSON
import logging  # Thư viện logging để ghi log thay cho print
from typing import List, Dict, Any  # Dùng để khai báo type hint cho code rõ ràng hơn

# Tạo logger cho module này.
# __name__ giúp xác định log đến từ file/module nào trong project
logger = logging.getLogger(__name__)


class UserNotFoundError(Exception):
    """Raised when a user cannot be found by email."""

    # Constructor của custom exception
    # email là dữ liệu gây ra lỗi
    def __init__(self, email: str):
        # Gọi constructor của class cha (Exception)
        # Message này sẽ xuất hiện khi exception được raise
        super().__init__(f"User with email {email} not found")

        # Lưu email gây lỗi vào object exception để debug hoặc log
        self.email = email


class UserManager:

    # Constructor của class
    # users là list các dictionary chứa thông tin user
    def __init__(self, users: List[Dict[str, Any]]):

        # Lưu danh sách user vào state của object
        # Ví dụ users:
        # [
        #   {"email": "a@test.com", "role": "admin"},
        #   {"email": "b@test.com", "role": "tester"}
        # ]
        self.users = users

    # Tìm user theo email
    def get_user_by_email(self, email: str) -> Dict[str, Any]:

        # Duyệt toàn bộ danh sách user
        for user in self.users:

            # user là dictionary
            # user.get("email") lấy giá trị key email
            # dùng .get() để tránh KeyError nếu key không tồn tại
            if user.get("email") == email:
                # Ghi log INFO khi tìm thấy user
                logger.info(f"User {email} found")

                # Trả về dictionary user
                return user

        # Nếu duyệt hết list mà không tìm thấy
        logger.error(f"User {email} not found")

        # Raise custom exception để báo lỗi
        raise UserNotFoundError(email)

    # Thêm user mới vào danh sách
    def add_user(self, email: str, role: str) -> None:

        # Ghi log INFO để trace hành động
        logger.info(f"Adding user {email}")

        # Thêm dictionary user mới vào list users
        self.users.append({"email": email, "role": role})

    # Xóa user theo email
    def remove_user_by_email(self, email: str) -> None:

        # Duyệt danh sách user
        for user in self.users:

            # Kiểm tra email
            if user.get("email") == email:
                # Log INFO khi xóa user
                logger.info(f"Removing user {email}")

                # Xóa user khỏi list
                self.users.remove(user)

                # return để dừng function ngay sau khi xóa
                return

        # Nếu không tìm thấy user để xóa
        logger.error(f"User {email} not found for removal")

        # Raise exception để báo lỗi
        raise UserNotFoundError(email)

    # Lưu danh sách user ra file JSON
    def save_to_file(self, filename: str) -> None:

        # Mở file ở chế độ write ("w")
        # encoding utf-8 để tránh lỗi ký tự
        with open(filename, "w", encoding="utf-8") as file:
            # json.dump chuyển Python object -> JSON
            # indent=4 giúp JSON format đẹp, dễ đọc
            json.dump(self.users, file, indent=4)

        # Log INFO khi lưu file thành công
        logger.info(f"Users saved to {filename}")


# Function helper để load users từ file JSON
def load_users_from_file(filename: str) -> List[Dict[str, Any]]:
    # Mở file JSON để đọc
    with open(filename, "r", encoding="utf-8") as file:
        # json.load chuyển JSON -> Python object
        data = json.load(file)

    # Validate dữ liệu:
    # JSON phải là list
    # nếu không -> raise lỗi
    if not isinstance(data, list):
        raise ValueError("users.json must contain a JSON array (list of users)")

    # Trả về danh sách users
    return data



