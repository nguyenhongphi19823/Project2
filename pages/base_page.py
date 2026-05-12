# import expect để dùng assertion của Playwright
from playwright.sync_api import expect


# class BasePage chứa các hàm dùng chung cho tất cả page
class BasePage:

    # constructor nhận page từ Playwright
    def __init__(self, page):

        # lưu page để các method khác dùng
        self.page = page


    # hàm click element
    def click(self, locator):

        # click vào element
        locator.click()


    # hàm nhập text vào input
    def fill(self, locator, value):

        # điền value vào locator
        locator.fill(value)


    # hàm kiểm tra element hiển thị
    def is_visible(self, locator):

        # assert element hiển thị
        expect(locator).to_be_visible()


    # hàm mở URL
    def open_url(self, url):

        # mở URL
        self.page.goto(url)


    # hàm chờ page load xong
    def wait_for_page_load(self):

        # chờ network idle
        self.page.wait_for_load_state("networkidle")


    # hàm kiểm tra URL không chứa text
    def assert_url_not_contains(self, text):

        # assert URL không chứa text
        assert text not in self.page.url