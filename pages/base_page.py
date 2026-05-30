# import expect để dùng assertion của Playwright
from playwright.sync_api import expect

#
# # class BasePage chứa các hàm dùng chung cho tất cả page
# class BasePage:
#
#     # constructor nhận page từ Playwright
#     def __init__(self, page):
#
#         # lưu page để các method khác dùng
#         self.page = page
#
#
#     # hàm click element
#     def click(self, locator):
#
#         # click vào element
#         locator.click()
#
#
#     # hàm nhập text vào input
#     def fill(self, locator, value):
#
#         # điền value vào locator
#         locator.fill(value)
#
#
#     # hàm kiểm tra element hiển thị
#     def is_visible(self, locator):
#
#         # assert element hiển thị
#         expect(locator).to_be_visible()
#
#
#     # hàm mở URL
#     def open_url(self, url):
#
#         # mở URL
#         self.page.goto(url)
#
#
#     # hàm chờ page load xong
#     def wait_for_page_load(self):
#
#         # chờ network idle
#         self.page.wait_for_load_state("networkidle")
#
#
#     # hàm kiểm tra URL không chứa text
#     def assert_url_not_contains(self, text):
#
#         # assert URL không chứa text
#         assert text not in self.page.url


# import expect để dùng assertion của Playwright
from playwright.sync_api import expect

# import get_logger để tạo logger cho BasePage
from utils.logger import get_logger


# tạo logger cho file base_page.py
logger = get_logger(__name__)


# class BasePage chứa action chung cho tất cả page
class BasePage:

    # constructor nhận page từ Playwright
    def __init__(self, page):

        # lưu page vào object để các method khác dùng
        self.page = page


    # method mở URL
    def open_url(self, url):

        # ghi log trước khi mở URL
        logger.info(f"Opening URL: {url}")

        # mở URL bằng Playwright
        self.page.goto(url)


    # method click element
    def click(self, locator):

        # ghi log trước khi click
        logger.info(f"Clicking locator: {locator}")

        # click vào locator
        locator.click()


    # method fill text vào input
    def fill(self, locator, value):

        # ghi log trước khi fill, không log password thật nếu value nhạy cảm
        logger.info(f"Filling locator: {locator}")

        # fill value vào locator
        locator.fill(value)


    # method kiểm tra element hiển thị
    def is_visible(self, locator):

        # ghi log trước khi verify visible
        logger.info(f"Verifying locator is visible: {locator}")

        # assert element hiển thị
        expect(locator).to_be_visible()


    # method chờ page load xong
    def wait_for_page_load(self):

        # ghi log trước khi chờ page load
        logger.info("Waiting for page load: networkidle")

        # chờ page load networkidle
        self.page.wait_for_load_state("networkidle")


    # method kiểm tra URL không chứa text
    def assert_url_not_contains(self, text):

        # ghi log trước khi kiểm tra URL
        logger.info(f"Verifying URL does not contain: {text}")

        # assert URL hiện tại không chứa text
        assert text not in self.page.url


