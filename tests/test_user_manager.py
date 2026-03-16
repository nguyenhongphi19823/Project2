# # Import class UserManager và custom exception để dùng trong test
# from app.user_manager import UserManager, UserNotFoundError
#
# # Import helper function để load dữ liệu user từ file JSON
# from app.user_manager import load_users_from_file
#
# # Load dữ liệu test từ file JSON
# # Hàm load_users_from_file sẽ đọc file app/users.json và trả về list user
# users = load_users_from_file("app/users.json")
#
#
# # Test case: kiểm tra khi email tồn tại
# def test_get_user_by_email_found():
#     # Tạo object UserManager với dữ liệu users
#     manager = UserManager(users)
#
#     # Gọi function cần test
#     user = manager.get_user_by_email("a@test.com")
#
#     # Kiểm tra kết quả trả về có đúng email mong đợi không
#     # Nếu đúng -> test pass
#     # Nếu sai -> pytest báo FAIL
#     assert user["email"] == "a@test.com"
#
#
# # Test case: kiểm tra khi email không tồn tại
# def test_get_user_by_email_not_found():
#     # Tạo object UserManager
#     manager = UserManager(users)
#
#     try:
#         # Gọi function với email không tồn tại
#         manager.get_user_by_email("x@test.com")
#
#         # Nếu không có exception xảy ra thì test phải FAIL
#         # vì chúng ta mong đợi function raise lỗi
#         assert False
#
#     except UserNotFoundError:
#         # Nếu bắt được đúng loại lỗi UserNotFoundError
#         # thì test PASS
#         assert True






# Import thư viện pytest để viết và chạy test
import pytest

# Import class UserManager (logic chính) và custom exception
# để dùng trong test
from app.user_manager import UserManager, UserNotFoundError

# Import helper function dùng để load dữ liệu user từ file JSON
from app.user_manager import load_users_from_file


# Fixture dùng để tạo object UserManager
# Fixture là một cơ chế của pytest giúp tạo data/setup
# và tái sử dụng cho nhiều test
@pytest.fixture
def manager():

    # Load dữ liệu test từ file JSON
    # Hàm load_users_from_file sẽ đọc file app/users.json
    # và trả về danh sách user dạng list
    users = load_users_from_file("app/users.json")

    # Tạo object UserManager với danh sách user vừa load
    # Fixture sẽ return object này cho các test dùng
    return UserManager(users)


# Test case: kiểm tra khi email tồn tại
# pytest sẽ tự động inject fixture "manager"
# vào parameter manager của function này
# def test_get_user_by_email_found(manager):
#
#     # Gọi function cần test
#     # tìm user có email "a@test.com"
#     user = manager.get_user_by_email("a@test.com")
#
#     # Kiểm tra kết quả trả về có đúng email mong đợi hay không
#     # Nếu đúng -> test PASS
#     # Nếu sai -> pytest báo FAIL
#     assert user["email"] == "a@test.com"

@pytest.mark.parametrize(
    "email, role",
    [
        ("a@test.com", "admin"),
        ("b@test.com", "tester"),
    ]
)
def test_get_user_role(manager, email, role):
    user = manager.get_user_by_email(email)
    assert user["role"] == role


# Test case: kiểm tra khi email không tồn tại
def test_get_user_by_email_not_found(manager):

    # pytest.raises dùng để kiểm tra một exception có được raise hay không
    # Nếu function không raise exception -> test FAIL
    # Nếu raise đúng loại exception -> test PASS
    with pytest.raises(UserNotFoundError):

        # Gọi function với email không tồn tại
        # Code trong UserManager sẽ raise UserNotFoundError
        manager.get_user_by_email("x@test.com")

