# Import module sys để làm việc với Python runtime
# Ở đây dùng để chỉnh sửa Python path (nơi Python tìm module)
import sys

# Import module os để làm việc với hệ điều hành
# Ví dụ: xử lý đường dẫn file, thư mục
import os


# Thêm đường dẫn project root vào Python path
# Điều này giúp Python tìm thấy module "app"
sys.path.append(
    os.path.abspath(                          # chuyển đường dẫn thành absolute path
        os.path.join(                         # nối các phần của đường dẫn
            os.path.dirname(__file__),        # lấy thư mục chứa file conftest.py
            ".."                              # ".." nghĩa là thư mục cha (project root)
        )
    )
)


# Import thư viện pytest để viết fixture và chạy test
# import pytest
#
#
# # Import class UserManager từ module app.user_manager
# # Class này chứa logic quản lý user
# from app.user_manager import UserManager
#
#
# # Import function helper để load dữ liệu user từ file JSON
# from app.user_manager import load_users_from_file
#
#
# # Khai báo fixture của pytest
# # Fixture này tạo object UserManager dùng chung cho các test
# @pytest.fixture
# def manager():
#
#     # Load dữ liệu test từ file JSON
#     # Hàm load_users_from_file sẽ đọc file app/users.json
#     # và trả về list các user
#     users = load_users_from_file("app/users.json")
#
#     # Tạo object UserManager với dữ liệu users
#     # Fixture sẽ return object này để test sử dụng
#     return UserManager(users)



# import pytest
# from app.user_manager import UserManager
# from app.user_manager import load_users_from_file

# import pytest để tạo fixture

import pytest

# import sync_playwright để điều khiển browser theo kiểu sync

from playwright.sync_api import sync_playwright

# import UserManager để dùng cho fixture manager cũ

from app.user_manager import UserManager

# import helper load dữ liệu từ JSON

from app.user_manager import load_users_from_file





# fixture manager dùng cho test Python/pytest hiện tại

@pytest.fixture(scope="module")

def manager():

    # load dữ liệu user từ file JSON

    users = load_users_from_file("app/users.json")

    # trả về object UserManager

    return UserManager(users)


# fixture playwright để khởi động Playwright engine

@pytest.fixture(scope="session")

def playwright_instance():

    # mở Playwright

    with sync_playwright() as p:

        # yield để cung cấp Playwright object cho test/fixture khác

        yield p




# fixture browser để mở browser 1 lần cho toàn bộ test session

@pytest.fixture(scope="session")

def browser(playwright_instance):

    # mở Chromium browser

    browser = playwright_instance.chromium.launch(headless=False)

    # yield browser cho test/fixture khác dùng

    yield browser

    # đóng browser sau khi toàn bộ test kết thúc

    browser.close()




# fixture page để tạo page mới cho mỗi test

@pytest.fixture(scope="function")

def page(browser):

    # tạo browser context mới

    # context giống như profile riêng biệt, giúp test độc lập

    context = browser.new_context()

    # tạo tab mới

    page = context.new_page()

    # yield page cho test dùng

    yield page

    # đóng context sau mỗi test để clean up

    context.close()





#
# @pytest.fixture(scope="module")
# def manager():
#     users = load_users_from_file("app/users.json")
#     return UserManager(users)



# import pytest
import pytest

# import thư viện xử lý thời gian
import time


# fixture tự chụp screenshot khi test fail
@pytest.fixture(autouse=True)

def screenshot_on_failure(request, page):

    # yield để test chạy trước
    yield

    # lấy kết quả test sau khi chạy xong
    if request.node.rep_call.failed:

        # tạo tên file screenshot theo timestamp
        screenshot_name = f"screenshots/{int(time.time())}.png"

        # chụp screenshot
        page.screenshot(path=screenshot_name)

        # in ra path để debug
        print(f"\nScreenshot saved: {screenshot_name}")




# hook của pytest để lấy kết quả test
@pytest.hookimpl(hookwrapper=True)

def pytest_runtest_makereport(item, call):

    # execute toàn bộ hook khác trước
    outcome = yield

    # lấy kết quả report
    rep = outcome.get_result()

    # lưu kết quả vào item
    setattr(item, "rep_" + rep.when, rep)