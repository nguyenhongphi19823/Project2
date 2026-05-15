# # import pytest để dùng parametrize
# import pytest
#
# # import LoginPage
# from pages.login_page import LoginPage
#
#
# # parametrize nhiều bộ data
# @pytest.mark.parametrize(
#     "username,password",
#     [
#
#         # account đúng
#         ("admin@test.com", "123456"),
#
#         # password sai
#         ("admin@test.com", "wrongpassword"),
#
#         # user không tồn tại
#         ("notfound@test.com", "123456"),
#     ]
# )
#
# # test login với nhiều data
# def test_login_multiple_data(page, username, password):
#
#     # tạo object LoginPage
#     login_page = LoginPage(page)
#
#     # mở login page
#     login_page.open()
#
#     # login bằng data hiện tại
#     login_page.login(username, password)
#
#     # chờ page load
#     login_page.wait_for_page_load()
#
#     # in URL hiện tại để debug
#     print(page.url)


# import pytest
import pytest

# import LoginPage
from pages.login_page import LoginPage

# import helper load JSON
from utils.data_loader import load_json_data


# load toàn bộ login data
login_test_data = load_json_data("test_data/login_data.json")


# parametrize bằng data từ JSON
@pytest.mark.parametrize("data", login_test_data)

def test_login_with_json_data(page, data):

    # tạo LoginPage
    login_page = LoginPage(page)

    # mở login page
    login_page.open()

    # login bằng data từ JSON
    login_page.login(
        data["username"],
        data["password"]
    )

    # chờ page load
    login_page.wait_for_page_load()

    # print URL để debug
    print(page.url)