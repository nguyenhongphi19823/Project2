# import expect để dùng assertion của Playwright
from playwright.sync_api import expect


# class đại diện cho trang Login
class LoginPage:

    # constructor nhận page từ Playwright
    def __init__(self, page):

        # lưu page vào self.page để các method khác dùng
        self.page = page

        # locator ô username
        self.username_input = page.get_by_placeholder("Enter your username or email")

        # locator ô password
        self.password_input = page.get_by_placeholder("Enter your password")

        # locator button Login
        self.login_button = page.get_by_role("button", name="Login")

        # locator text/link Forgot your password
        self.forgot_password_link = page.get_by_text("Forgot your password?")

    # method mở trang login
    def open(self):

        # mở URL login của DP360
        self.page.goto("https://app.dp360crm.com/login")

    # method kiểm tra UI login hiển thị đúng
    def verify_login_page_is_visible(self):

        # kiểm tra ô username hiển thị
        expect(self.username_input).to_be_visible()

        # kiểm tra ô password hiển thị
        expect(self.password_input).to_be_visible()

        # kiểm tra button Login hiển thị
        expect(self.login_button).to_be_visible()

        # kiểm tra link Forgot your password hiển thị
        expect(self.forgot_password_link).to_be_visible()

    # method login
    def login(self, username, password):

        # điền username
        self.username_input.fill(username)

        # điền password
        self.password_input.fill(password)

        # click button Login
        self.login_button.click()