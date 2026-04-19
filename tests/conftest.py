# Import module sys để làm việc với Python runtime
# Ở đây dùng để chỉnh sửa Python path (nơi Python tìm module)
import sys

# Import module os để làm việc với hệ điều hành
# Ví dụ: xử lý đường dẫn file, thư mục
import os


# Thêm đường dẫn project root vào Python path
# Điều này giúp Python tìm thấy module "app"
sys.path.append(
    os.path.abspath(                          # chuyển đường dẫn thành absolute path
        os.path.join(                         # nối các phần của đường dẫn
            os.path.dirname(__file__),        # lấy thư mục chứa file conftest.py
            ".."                              # ".." nghĩa là thư mục cha (project root)
        )
    )
)


# Import thư viện pytest để viết fixture và chạy test
# import pytest
#
#
# # Import class UserManager từ module app.user_manager
# # Class này chứa logic quản lý user
# from app.user_manager import UserManager
#
#
# # Import function helper để load dữ liệu user từ file JSON
# from app.user_manager import load_users_from_file
#
#
# # Khai báo fixture của pytest
# # Fixture này tạo object UserManager dùng chung cho các test
# @pytest.fixture
# def manager():
#
#     # Load dữ liệu test từ file JSON
#     # Hàm load_users_from_file sẽ đọc file app/users.json
#     # và trả về list các user
#     users = load_users_from_file("app/users.json")
#
#     # Tạo object UserManager với dữ liệu users
#     # Fixture sẽ return object này để test sử dụng
#     return UserManager(users)



import pytest
from app.user_manager import UserManager
from app.user_manager import load_users_from_file

@pytest.fixture(scope="module")
def manager():
    users = load_users_from_file("app/users.json")
    return UserManager(users)