# Import class UserManager và custom exception để dùng trong test
from app.user_manager import UserManager, UserNotFoundError

# Import helper function để load dữ liệu user từ file JSON
from app.user_manager import load_users_from_file

# Load dữ liệu test từ file JSON
# Hàm load_users_from_file sẽ đọc file app/users.json và trả về list user
users = load_users_from_file("app/users.json")


# Test case: kiểm tra khi email tồn tại
def test_get_user_by_email_found():
    # Tạo object UserManager với dữ liệu users
    manager = UserManager(users)

    # Gọi function cần test
    user = manager.get_user_by_email("a@test.com")

    # Kiểm tra kết quả trả về có đúng email mong đợi không
    # Nếu đúng -> test pass
    # Nếu sai -> pytest báo FAIL
    assert user["email"] == "a@test.com"


# Test case: kiểm tra khi email không tồn tại
def test_get_user_by_email_not_found():
    # Tạo object UserManager
    manager = UserManager(users)

    try:
        # Gọi function với email không tồn tại
        manager.get_user_by_email("x@test.com")

        # Nếu không có exception xảy ra thì test phải FAIL
        # vì chúng ta mong đợi function raise lỗi
        assert False

    except UserNotFoundError:
        # Nếu bắt được đúng loại lỗi UserNotFoundError
        # thì test PASS
        assert True