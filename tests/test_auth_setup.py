# import os để đọc username/password từ .env
import os

# import load_dotenv để load file .env
from dotenv import load_dotenv

# import LoginPage để dùng Page Object login
from pages.login_page import LoginPage


# load file .env ở root project
load_dotenv()


# test setup auth dùng để login và lưu storage state
def test_save_login_state(page):

    # đọc username từ .env
    username = os.getenv("DP360_USERNAME")

    # đọc password từ .env
    password = os.getenv("DP360_PASSWORD")

    # kiểm tra username không bị thiếu
    assert username, "DP360_USERNAME is missing"

    # kiểm tra password không bị thiếu
    assert password, "DP360_PASSWORD is missing"

    # tạo object LoginPage
    login_page = LoginPage(page)

    # mở trang login
    login_page.open()

    # login bằng username/password thật
    login_page.login(username, password)

    # chờ trang load xong sau login
    login_page.wait_for_page_load()

    # kiểm tra login thành công bằng cách URL không còn chứa /login
    assert "/login" not in page.url

    # lưu cookies/localStorage/session vào file storage_state.json
    page.context.storage_state(path="auth/storage_state.json")