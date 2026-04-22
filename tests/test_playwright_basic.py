# import pytest để dùng fixture
import pytest

# import sync_playwright để điều khiển browser
from playwright.sync_api import sync_playwright


# test đầu tiên
def test_open_google():

    # khởi động Playwright
    with sync_playwright() as p:

        # mở browser Chromium (giống Chrome)
        browser = p.chromium.launch(headless=False)
        # headless=False để nhìn thấy browser (debug dễ hơn)

        # tạo context (giống profile riêng)
        context = browser.new_context()

        # tạo tab mới (page)
        page = context.new_page()

        # mở website Google
        page.goto("https://www.google.com")

        # chờ 3 giây để nhìn thấy browser
        page.wait_for_timeout(3000)


        browser.close()