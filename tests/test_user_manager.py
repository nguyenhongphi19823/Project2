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



#
#
#
# # Import thư viện pytest để viết và chạy test
# import pytest
#
# # Import class UserManager (logic chính) và custom exception
# # để dùng trong test
# from app.user_manager import UserManager, UserNotFoundError
#
# # Import helper function dùng để load dữ liệu user từ file JSON
# from app.user_manager import load_users_from_file
#
#
# # Fixture dùng để tạo object UserManager
# # Fixture là một cơ chế của pytest giúp tạo data/setup
# # và tái sử dụng cho nhiều test
# @pytest.fixture
# def manager():
#
#     # Load dữ liệu test từ file JSON
#     # Hàm load_users_from_file sẽ đọc file app/users.json
#     # và trả về danh sách user dạng list
#     users = load_users_from_file("app/users.json")
#
#     # Tạo object UserManager với danh sách user vừa load
#     # Fixture sẽ return object này cho các test dùng
#     return UserManager(users)
#
#
# # Test case: kiểm tra khi email tồn tại
# # pytest sẽ tự động inject fixture "manager"
# # vào parameter manager của function này
# # def test_get_user_by_email_found(manager):
# #
# #     # Gọi function cần test
# #     # tìm user có email "a@test.com"
# #     user = manager.get_user_by_email("a@test.com")
# #
# #     # Kiểm tra kết quả trả về có đúng email mong đợi hay không
# #     # Nếu đúng -> test PASS
# #     # Nếu sai -> pytest báo FAIL
# #     assert user["email"] == "a@test.com"
#
#
#
#
# # Test case: kiểm tra khi email không tồn tại
# # def test_get_user_by_email_not_found(manager):
# #
# #     # pytest.raises dùng để kiểm tra một exception có được raise hay không
# #     # Nếu function không raise exception -> test FAIL
# #     # Nếu raise đúng loại exception -> test PASS
# #     with pytest.raises(UserNotFoundError):
# #
# #         # Gọi function với email không tồn tại
# #         # Code trong UserManager sẽ raise UserNotFoundError
# #         manager.get_user_by_email("x@test.com")
#
#
#
# # pytest.mark.parametrize dùng để chạy cùng một test với nhiều bộ dữ liệu khác nhau
# @pytest.mark.parametrize(
#
#     # Khai báo tên các biến sẽ được truyền vào test function
#     # Ở đây test sẽ nhận 2 biến: email và role
#     "email, role",
#
#     # Danh sách các bộ dữ liệu test
#     # Mỗi tuple sẽ tạo ra 1 lần chạy test
#     [
#         ("a@test.com", "admin"),   # Lần chạy test 1
#         ("b@test.com", "tester"),  # Lần chạy test 2
#     ]
# )
#
# # Test function
# # pytest sẽ inject:
# # - fixture "manager"
# # - dữ liệu email và role từ parametrize
# def test_get_user_role(manager, email, role):
#
#     # Gọi function cần test
#     # tìm user theo email
#     user = manager.get_user_by_email(email)
#
#     # Kiểm tra role của user trả về có đúng như mong đợi không
#     # Nếu đúng -> test PASS
#     # Nếu sai -> pytest báo FAIL
#     assert user["role"] == role
#
#
#
#
# # pytest.mark.parametrize dùng để chạy cùng một test với nhiều bộ dữ liệu
# @pytest.mark.parametrize(
#
#     # Khai báo tên biến sẽ được truyền vào test function
#     # Ở đây test function sẽ nhận biến "email"
#     "email",
#
#     # Danh sách dữ liệu test
#     # Mỗi giá trị trong list sẽ tạo ra 1 lần chạy test
#     [
#         "x@test.com",  # Test case 1
#         "y@test.com",  # Test case 2
#         "z@test.com",  # Test case 3
#     ]
# )
#
# # Test function
# # pytest sẽ inject:
# # - fixture "manager"
# # - biến email từ parametrize
# def test_user_not_found(manager, email):
#
#     # pytest.raises dùng để kiểm tra một exception có được raise hay không
#     # Nếu code bên trong không raise exception -> test FAIL
#     # Nếu raise đúng loại exception -> test PASS
#     with pytest.raises(UserNotFoundError):
#
#         # Gọi function cần test với email không tồn tại
#         # Trong UserManager, hàm get_user_by_email sẽ raise UserNotFoundError
#         manager.get_user_by_email(email)
#
#


# Import thư viện pytest để sử dụng các tính năng của pytest
# như parametrize, raises, fixture injection
import pytest

# Import custom exception từ module user_manager
# Exception này sẽ được raise khi không tìm thấy user
from app.user_manager import UserNotFoundError


# Test case: kiểm tra khi email tồn tại trong danh sách user
# pytest sẽ tự động inject fixture "manager" từ conftest.py
def test_get_user_by_email_found(manager):

    # Gọi method get_user_by_email để tìm user theo email
    user = manager.get_user_by_email("a@test.com")

    # Kiểm tra role của user trả về có đúng là "admin" hay không
    # Nếu đúng -> test PASS
    # Nếu sai -> pytest báo FAIL
    assert user["role"] == "admin"


# pytest.mark.parametrize cho phép chạy cùng một test
# với nhiều bộ dữ liệu khác nhau
@pytest.mark.parametrize(

    # Tên biến sẽ được truyền vào test function
    # Ở đây test function sẽ nhận biến "email"
    "email",

    # Danh sách dữ liệu test
    # Mỗi phần tử trong list sẽ tạo ra một lần chạy test
    [
        "x@test.com",  # Test case 1
        "y@test.com",  # Test case 2
        "z@test.com",  # Test case 3
    ]
)

# Test case: kiểm tra khi email không tồn tại
# pytest sẽ inject:
# - fixture manager
# - biến email từ parametrize
def test_user_not_found(manager, email):

    # pytest.raises dùng để kiểm tra một exception có được raise hay không
    # Nếu code bên trong không raise exception -> test FAIL
    # Nếu raise đúng exception -> test PASS
    with pytest.raises(UserNotFoundError):

        # Gọi function với email không tồn tại
        # Trong UserManager, method này sẽ raise UserNotFoundError
        manager.get_user_by_email(email)