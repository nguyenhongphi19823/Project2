import sys
import time
from pathlib import Path

import pytest
from playwright.sync_api import sync_playwright

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from app.user_manager import UserManager, load_users_from_file
from config.settings import BROWSER, HEADLESS


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
    with sync_playwright() as playwright:
        yield playwright


@pytest.fixture(scope="session")
def browser(playwright_instance):
    browser_name = BROWSER.lower()

    if browser_name == "chromium":
        browser_obj = playwright_instance.chromium.launch(headless=HEADLESS)
    elif browser_name == "firefox":
        browser_obj = playwright_instance.firefox.launch(headless=HEADLESS)
    elif browser_name == "webkit":
        browser_obj = playwright_instance.webkit.launch(headless=HEADLESS)
    else:
        raise ValueError(f"Unsupported browser: {BROWSER}")

    yield browser_obj
    browser_obj.close()


@pytest.fixture(scope="function")
def page(browser, request):
    context = browser.new_context(
        record_video_dir=str(VIDEOS_DIR),
        record_video_size={"width": 1280, "height": 720},
    )
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    page_obj = context.new_page()
    yield page_obj

    report = getattr(request.node, "rep_call", None)
    if report and report.failed:
        screenshot_name = SCREENSHOTS_DIR / f"{int(time.time())}.png"
        page_obj.screenshot(path=str(screenshot_name))
        print(f"\nScreenshot saved: {screenshot_name}")

    context.tracing.stop(path=str(TRACES_DIR / "trace.zip"))
    context.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)


@pytest.fixture(scope="function")
def api_context(playwright_instance):
    context = playwright_instance.request.new_context()
    yield context
    context.dispose()


@pytest.fixture(scope="function")
def logged_in_page(browser):
    context = browser.new_context(storage_state="auth/storage_state.json")
    page_obj = context.new_page()
    yield page_obj
    context.close()




# import allure để attach file vào report
import allure

# import pytest để dùng fixture và hook
import pytest

# import time để tạo tên file theo timestamp
import time

# import os để tạo folder nếu chưa có
import os


# tạo folder screenshots nếu chưa có
os.makedirs("screenshots", exist_ok=True)


# fixture tự động chạy cho mỗi test
@pytest.fixture(autouse=True)
def attach_screenshot_on_failure(request, page):

    # cho test chạy trước
    yield

    # kiểm tra test có bị fail ở phase call không
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:

        # tạo đường dẫn screenshot
        screenshot_path = f"screenshots/{request.node.name}_{int(time.time())}.png"

        # chụp screenshot
        page.screenshot(path=screenshot_path, full_page=True)

        # mở file screenshot dạng binary
        with open(screenshot_path, "rb") as image_file:

            # attach screenshot vào Allure report
            allure.attach(
                image_file.read(),
                name="failure_screenshot",
                attachment_type=allure.attachment_type.PNG
            )


# hook lấy kết quả pass/fail của từng phase test
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    # chạy các hook khác trước
    outcome = yield

    # lấy report result
    rep = outcome.get_result()

    # gắn report vào item để fixture đọc được
    setattr(item, "rep_" + rep.when, rep)