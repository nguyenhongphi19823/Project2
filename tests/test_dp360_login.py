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




    # điền username vào ô username
    page.locator("input[name='Username']").fill(username)




    # điền password vào ô password
    page.locator("input[name='Password']").fill(password)

    # click nút login
    page.locator("button[type='submit']").click()



    # kiểm tra sau login URL không còn là trang login
    expect(page).not_to_have_url("https://app.dp360crm.com/")

