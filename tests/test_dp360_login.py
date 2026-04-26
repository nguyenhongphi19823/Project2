# import os để đọc username/password từ environment variable
import os

# import expect để assertion theo kiểu Playwright
from playwright.sync_api import expect


# test login vào DP360 CRM
def test_dp360_login(page):



    # đọc username từ environment variable
    username = os.getenv("DP360_USERNAME")



    # đọc password từ environment variable
    password = os.getenv("DP360_PASSWORD")


    # kiểm tra username không bị None hoặc rỗng
    assert username, "DP360_USERNAME is missing"


    # kiểm tra password không bị None hoặc rỗng
    assert password, "DP360_PASSWORD is missing"

    # mở trang login DP360 CRM
    page.goto("https://app.dp360crm.com")




    # # điền username vào ô username
    # page.locator("input[name='Username']").fill(username)
    #
    # # điền password vào ô password
    # page.locator("input[name='Password']").fill(password)
    #
    # # click nút login
    # page.locator("button[type='submit']").click()


    # chờ ô username hiển thị trên màn hình
    username_input = page.get_by_placeholder("Enter your username or email")


    # điền username vào ô username
    username_input.fill(username)

    # chờ ô password hiển thị trên màn hình
    password_input = page.get_by_placeholder("Enter your password")

    # điền password vào ô password
    password_input.fill(password)

    # click nút Login theo role button và tên hiển thị
    page.get_by_role("button", name="Login").click()


    # chờ trang chuyển hướng sau khi login
    page.wait_for_load_state("networkidle")


    # # kiểm tra URL sau login không còn chứa /login
    # expect(page).not_to_have_url(lambda url: "/login" in url)

    # kiểm tra URL hiện tại không còn chứa "/login"
    assert "/login" not in page.url




    # # kiểm tra sau login URL không còn là trang login
    # expect(page).not_to_have_url("https://app.dp360crm.com/")

