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