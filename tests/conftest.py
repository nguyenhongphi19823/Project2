import sys
import time
from pathlib import Path

import pytest
from playwright.sync_api import sync_playwright

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_ROOT))

from app.user_manager import UserManager, load_users_from_file


SCREENSHOTS_DIR = PROJECT_ROOT / "screenshots"
TRACES_DIR = PROJECT_ROOT / "traces"
VIDEOS_DIR = PROJECT_ROOT / "videos"

for artifact_dir in (SCREENSHOTS_DIR, TRACES_DIR, VIDEOS_DIR):
    artifact_dir.mkdir(exist_ok=True)


@pytest.fixture(scope="module")
def manager():
    users = load_users_from_file("app/users.json")
    return UserManager(users)


@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p


@pytest.fixture(scope="session")
def browser(playwright_instance):
    browser = playwright_instance.chromium.launch(headless=False)
    yield browser
    browser.close()


@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context(
        record_video_dir=str(VIDEOS_DIR),
        record_video_size={"width": 1280, "height": 720},
    )
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    page = context.new_page()
    yield page

    context.tracing.stop(path=str(TRACES_DIR / "trace.zip"))
    context.close()


@pytest.fixture(autouse=True)
def screenshot_on_failure(request):
    yield

    if request.node.rep_call.failed and "page" in request.fixturenames:
        page = request.getfixturevalue("page")
        screenshot_name = SCREENSHOTS_DIR / f"{int(time.time())}.png"
        page.screenshot(path=str(screenshot_name))
        print(f"\nScreenshot saved: {screenshot_name}")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)



# fixture API context
@pytest.fixture(scope="function")

def api_context(playwright):

    # tạo context
    context = playwright.request.new_context()

    # yield cho test dùng
    yield context

    # cleanup
    context.dispose()


# import pytest để tạo fixture
import pytest


# fixture tạo page đã login sẵn
@pytest.fixture(scope="function")
def logged_in_page(browser):

    # tạo context mới và load storage_state đã lưu
    context = browser.new_context(
        # dùng file auth/storage_state.json để khôi phục login session
        storage_state="auth/storage_state.json"
    )

    # tạo tab mới từ context đã login
    page = context.new_page()

    # yield page cho test sử dụng
    yield page

    # đóng context sau khi test xong để clean up
    context.close()



# import pytest để tạo fixture
import pytest

# import sync_playwright để dùng Playwright
from playwright.sync_api import sync_playwright

# import HEADLESS và BROWSER từ config
from config.settings import HEADLESS, BROWSER


# fixture khởi động Playwright engine
@pytest.fixture(scope="session")
def playwright_instance():

    # mở Playwright
    with sync_playwright() as p:

        # trả Playwright object cho fixture khác
        yield p


# fixture browser dùng cho toàn bộ test session
@pytest.fixture(scope="session")
def browser(playwright_instance):

    # nếu BROWSER là chromium thì mở chromium
    if BROWSER == "chromium":

        # launch chromium với headless lấy từ config
        browser = playwright_instance.chromium.launch(headless=HEADLESS)

    # nếu BROWSER là firefox thì mở firefox
    elif BROWSER == "firefox":

        # launch firefox với headless lấy từ config
        browser = playwright_instance.firefox.launch(headless=HEADLESS)

    # nếu BROWSER là webkit thì mở webkit
    elif BROWSER == "webkit":

        # launch webkit với headless lấy từ config
        browser = playwright_instance.webkit.launch(headless=HEADLESS)

    # nếu BROWSER không hợp lệ thì báo lỗi
    else:

        # raise lỗi rõ ràng
        raise ValueError(f"Unsupported browser: {BROWSER}")

    # trả browser cho test dùng
    yield browser

    # đóng browser sau khi toàn bộ test chạy xong
    browser.close()



# import pytest để dùng fixture và hook của pytest
import pytest


# hook pytest_addoption dùng để thêm custom command line option
def pytest_addoption(parser):

    # thêm option --browser vào pytest command
    parser.addoption(
        # tên option khi chạy command line
        "--browser",

        # action="store" nghĩa là lưu giá trị người dùng truyền vào
        action="store",

        # giá trị mặc định nếu user không truyền --browser
        default="chromium",

        # mô tả option này dùng để làm gì
        help="Browser to run tests: chromium, firefox, or webkit"
    )

    # thêm option --headless vào pytest command
    parser.addoption(
        # tên option khi chạy command line
        "--headless",

        # action="store" nghĩa là lưu giá trị người dùng truyền vào
        action="store",

        # giá trị mặc định nếu user không truyền --headless
        default="false",

        # mô tả option này dùng để làm gì
        help="Run browser in headless mode: true or false"
    )


# fixture browser dùng cho toàn bộ test session
@pytest.fixture(scope="session")
def browser(playwright_instance, request):

    # lấy giá trị browser từ command line option --browser
    browser_name = request.config.getoption("--browser")

    # lấy giá trị headless từ command line option --headless
    headless_value = request.config.getoption("--headless")

    # convert string "true"/"false" thành boolean True/False
    headless = headless_value.lower() == "true"

    # nếu browser_name là chromium
    if browser_name == "chromium":

        # mở Chromium browser
        browser = playwright_instance.chromium.launch(headless=headless)

    # nếu browser_name là firefox
    elif browser_name == "firefox":

        # mở Firefox browser
        browser = playwright_instance.firefox.launch(headless=headless)

    # nếu browser_name là webkit
    elif browser_name == "webkit":

        # mở WebKit browser
        browser = playwright_instance.webkit.launch(headless=headless)

    # nếu browser_name không hợp lệ
    else:

        # báo lỗi rõ ràng để dễ debug
        raise ValueError(f"Unsupported browser: {browser_name}")

    # trả browser cho các test sử dụng
    yield browser

    # đóng browser sau khi toàn bộ test session kết thúc
    browser.close()