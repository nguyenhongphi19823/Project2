# import pytest để dùng fixture
import pytest

# import sync_playwright để điều khiển browser
# from playwright.sync_api import sync_playwright
#
#
# # test đầu tiên
# def test_open_google():
#
#     # khởi động Playwright
#     with sync_playwright() as p:
#
#         # mở browser Chromium (giống Chrome)
#         browser = p.chromium.launch(headless=False)
#         # headless=False để nhìn thấy browser (debug dễ hơn)
#
#         # tạo context (giống profile riêng)
#         context = browser.new_context()
#
#         # tạo tab mới (page)
#         page = context.new_page()
#
#         # mở website Google
#         page.goto("https://www.google.com")
#
#         # chờ 3 giây để nhìn thấy browser
#         page.wait_for_timeout(3000)
#
#         # đóng browser
#         browser.close()


# test mở website đầu tiên bằng fixture page
def test_open_example(page):

    # mở website example
    page.goto("https://example.com")

    # kiểm tra title của trang có chứa chữ Example không
    assert "Example" in page.title()


# test kiểm tra nội dung heading trên trang example
def test_example_heading(page):

    # mở website example
    page.goto("https://example.com")

    # lấy text của thẻ h1
    heading = page.locator("h1").text_content()

    # kiểm tra heading đúng
    assert heading == "Example Domain"