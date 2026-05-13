# import pytest để dùng parametrize
import pytest

# import LoginPage
from pages.login_page import LoginPage


# parametrize nhiều bộ data
@pytest.mark.parametrize(
    "username,password",
    [

        # account đúng
        ("admin@test.com", "123456"),

        # password sai
        ("admin@test.com", "wrongpassword"),

        # user không tồn tại
        ("notfound@test.com", "123456"),
    ]
)

# test login với nhiều data
def test_login_multiple_data(page, username, password):

    # tạo object LoginPage
    login_page = LoginPage(page)

    # mở login page
    login_page.open()

    # login bằng data hiện tại
    login_page.login(username, password)

    # chờ page load
    login_page.wait_for_page_load()

    # in URL hiện tại để debug
    print(page.url)