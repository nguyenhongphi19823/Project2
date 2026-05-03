# import os để đọc biến môi trường
import os
# import re để dùng regular expression trong assertion URL
import re
# import LoginPage từ pages/login_page.py
from pages.login_page import LoginPage
# import load_dotenv để load dữ liệu từ file .env
from dotenv import load_dotenv
# import expect để dùng assertion của Playwright
from playwright.sync_api import expect
# load file .env ở root project
load_dotenv()

# # test kiểm tra form login hiển thị đúng
# def test_dp360_login_page_ui(page):
#     # mở trang login DP360 CRM
#     page.goto("https://app.dp360crm.com")
#     # đặt kích thước trình duyệt ở chế độ xem tối đa
#     page.set_viewport_size({"width": 1920, "height": 1080})
#     # kiểm tra ô username hiển thị
#     expect(page.get_by_placeholder("Enter your username or email")).to_be_visible()
#     # kiểm tra ô password hiển thị
#     expect(page.get_by_placeholder("Enter your password")).to_be_visible()
#     # kiểm tra nút Login hiển thị
#     expect(page.get_by_role("button", name="Login")).to_be_visible()
#     # kiểm tra text Forgot your password hiển thị
#     expect(page.get_by_text("Forgot your password?")).to_be_visible()

# test kiểm tra UI login page
def test_dp360_login_page_ui(page):
    # tạo object LoginPage
    login_page = LoginPage(page)
    # mở trang login
    login_page.open()
    # kiểm tra UI login hiển thị đúng
    login_page.verify_login_page_is_visible()

# test login vào DP360 CRM
# def test_dp360_login(page):
#     # đọc username từ environment variable
#     username = os.getenv("DP360_USERNAME")
#     # đọc password từ environment variable
#     password = os.getenv("DP360_PASSWORD")
#     # kiểm tra username không bị None hoặc rỗng
#     assert username, "DP360_USERNAME is missing"
#     # kiểm tra password không bị None hoặc rỗng
#     assert password, "DP360_PASSWORD is missing"
#     # mở trang login DP360 CRM
#     page.goto("https://app.dp360crm.com")
#     # đặt kích thước trình duyệt ở chế độ xem tối đa
#     page.set_viewport_size({"width": 1920, "height": 1080})
#     # assert ô username hiển thị trước khi fill
#     expect(page.get_by_placeholder("Enter your username or email")).to_be_visible()
#     # điền username
#     page.get_by_placeholder("Enter your username or email").fill(username)
#     # assert ô password hiển thị trước khi fill
#     expect(page.get_by_placeholder("Enter your password")).to_be_visible()
#     # điền password
#     page.get_by_placeholder("Enter your password").fill(password)
#     # assert nút Login hiển thị và enabled
#     expect(page.get_by_role("button", name="Login")).to_be_enabled()
#     # click Login
#     page.get_by_role("button", name="Login").click()
#     # chờ trang chuyển hướng sau khi login
#     page.wait_for_load_state("networkidle")
#     # kiểm tra URL không còn là login page
#     expect(page).not_to_have_url(re.compile(r".*/login.*"))

# test login DP360 CRM
def test_dp360_login(page):
    # đọc username từ .env
    username = os.getenv("DP360_USERNAME")
    # đọc password từ .env
    password = os.getenv("DP360_PASSWORD")
    # kiểm tra username có tồn tại không
    assert username, "DP360_USERNAME is missing"
    # kiểm tra password có tồn tại không
    assert password, "DP360_PASSWORD is missing"
    # tạo object LoginPage
    login_page = LoginPage(page)
    # mở trang login
    login_page.open()
    # đặt kích thước trình duyệt ở chế độ xem tối đa
    page.set_viewport_size({"width": 1920, "height": 1080})
    # thực hiện login
    login_page.login(username, password)
    # chờ trang load xong sau khi login
    page.wait_for_load_state("networkidle")
    # kiểm tra URL sau login không còn chứa /login
    assert "/login" not in page.url
