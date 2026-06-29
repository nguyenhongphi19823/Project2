# import sys để thêm project root vào Python path
import sys

# import time để tạo tên file screenshot/trace theo timestamp
import time

# import Path để xử lý đường dẫn file/folder tốt hơn
from pathlib import Path

# import pytest để tạo fixture và hook
import pytest

# import allure để attach screenshot vào Allure report khi test fail
import allure

# import sync_playwright để tự khởi động Playwright
from playwright.sync_api import sync_playwright


# lấy đường dẫn root project, tức là folder Project2
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# kiểm tra PROJECT_ROOT đã có trong sys.path chưa
if str(PROJECT_ROOT) not in sys.path:

    # thêm PROJECT_ROOT vào sys.path để import app/pages/config không bị lỗi
    sys.path.insert(0, str(PROJECT_ROOT))


# import UserManager và load_users_from_file sau khi đã add PROJECT_ROOT vào sys.path
from app.user_manager import UserManager, load_users_from_file

# import BROWSER và HEADLESS từ config để dùng làm fallback/default
from config.settings import BROWSER, HEADLESS


# khai báo folder lưu screenshot
SCREENSHOTS_DIR = PROJECT_ROOT / "screenshots"

# khai báo folder lưu trace
TRACES_DIR = PROJECT_ROOT / "traces"

# khai báo folder lưu video
VIDEOS_DIR = PROJECT_ROOT / "videos"


# duyệt qua từng folder artifact cần tạo
for artifact_dir in (SCREENSHOTS_DIR, TRACES_DIR, VIDEOS_DIR):

    # tạo folder nếu folder chưa tồn tại
    artifact_dir.mkdir(exist_ok=True)


# hook thêm custom option cho pytest
def pytest_addoption(parser):

    # thêm option --headless vì --browser đã có sẵn từ pytest-playwright
    parser.addoption("--headless", action="store", default=str(HEADLESS).lower())


# hook lấy kết quả pass/fail của từng phase trong test
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    # cho pytest chạy hook gốc trước
    outcome = yield

    # lấy kết quả report của phase hiện tại
    rep = outcome.get_result()

    # gắn report vào item, ví dụ rep_call, rep_setup, rep_teardown
    setattr(item, "rep_" + rep.when, rep)


# fixture tạo UserManager dùng cho test logic Python
@pytest.fixture(scope="module")
def manager():

    # load users từ file app/users.json
    users = load_users_from_file("app/users.json")

    # trả về object UserManager
    return UserManager(users)


# fixture khởi động Playwright một lần cho cả test session
@pytest.fixture(scope="session")
def playwright_instance():

    # mở Playwright bằng context manager
    with sync_playwright() as playwright:

        # trả Playwright object cho các fixture khác dùng
        yield playwright


# fixture browser dùng cho toàn bộ test session
@pytest.fixture(scope="session")
def browser(playwright_instance, request):

    # lấy giá trị --browser từ pytest-playwright
    browser_option = request.config.getoption("--browser", default=BROWSER)

    # nếu browser_option là list thì lấy browser đầu tiên
    if isinstance(browser_option, list):

        # lấy phần tử đầu tiên trong list browser
        browser_name = browser_option[0]

    # nếu browser_option là string thì dùng trực tiếp
    else:

        # gán browser_option vào browser_name
        browser_name = browser_option

    # lấy giá trị --headless từ command line
    headless_value = request.config.getoption("--headless")

    # convert giá trị headless thành string rồi lower để xử lý chắc chắn
    headless_text = str(headless_value).lower()

    # convert "true"/"false" thành boolean True/False
    headless = headless_text == "true"

    # nếu browser là chromium
    if browser_name == "chromium":

        # mở Chromium browser
        browser_obj = playwright_instance.chromium.launch(headless=headless)

    # nếu browser là firefox
    elif browser_name == "firefox":

        # mở Firefox browser
        browser_obj = playwright_instance.firefox.launch(headless=headless)

    # nếu browser là webkit
    elif browser_name == "webkit":

        # mở WebKit browser
        browser_obj = playwright_instance.webkit.launch(headless=headless)

    # nếu browser không thuộc 3 loại trên
    else:

        # báo lỗi rõ ràng để dễ debug
        raise ValueError(f"Unsupported browser: {browser_name}")

    # trả browser cho các test sử dụng
    yield browser_obj

    # đóng browser sau khi test session kết thúc
    browser_obj.close()


# fixture page dùng cho từng test UI
@pytest.fixture(scope="function")
def page(browser, request, worker_id):

    # tạo browser context mới cho từng test và bật record video
    context = browser.new_context(
        record_video_dir=str(VIDEOS_DIR),
        record_video_size={"width": 1280, "height": 720},
    )

    # bật tracing để lưu thao tác, screenshot, DOM snapshot, source
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    # tạo page/tab mới
    page_obj = context.new_page()

    # trả page cho test chạy
    yield page_obj

    # lấy report của phase call sau khi test chạy xong
    report = getattr(request.node, "rep_call", None)

    # lấy tên test và thay ký tự dễ gây lỗi bằng dấu gạch dưới
    test_name = request.node.name.replace("[", "_").replace("]", "_").replace("/", "_")

    # thêm worker_id vào tên file để tránh trùng khi chạy parallel
    test_name = f"{worker_id}_{test_name}"

    # tạo timestamp để tên file không bị trùng
    timestamp = int(time.time())

    # kiểm tra test có bị fail không
    is_failed = report is not None and report.failed

    # nếu test bị fail
    if is_failed:

        # tạo đường dẫn screenshot fail
        screenshot_path = SCREENSHOTS_DIR / f"{test_name}_{timestamp}.png"

        # chụp screenshot full page
        page_obj.screenshot(path=str(screenshot_path), full_page=True)

        # in ra đường dẫn screenshot trong terminal
        print(f"\nScreenshot saved: {screenshot_path}")

        # mở file screenshot dạng binary
        with open(screenshot_path, "rb") as image_file:

            # attach screenshot vào Allure report
            allure.attach(
                image_file.read(),
                name="failure_screenshot",
                attachment_type=allure.attachment_type.PNG,
            )

    # tạo đường dẫn trace riêng cho từng test
    trace_path = TRACES_DIR / f"{test_name}_{timestamp}.zip"

    # dừng tracing và lưu trace ra file
    context.tracing.stop(path=str(trace_path))

    # in ra đường dẫn trace trong terminal
    print(f"\nTrace saved: {trace_path}")

    # đóng context để video được finalize
    context.close()


# fixture API context dùng cho API testing
@pytest.fixture(scope="function")
def api_context(playwright_instance):

    # tạo API request context
    context = playwright_instance.request.new_context()

    # trả API context cho test dùng
    yield context

    # đóng API context sau khi test xong
    context.dispose()


# fixture tạo page đã login sẵn bằng storage_state
@pytest.fixture(scope="function")
def logged_in_page(browser):

    # tạo context mới và load storage state đã lưu
    context = browser.new_context(storage_state="auth/storage_state.json")

    # tạo page mới từ context đã login
    page_obj = context.new_page()

    # trả page đã login cho test dùng
    yield page_obj

    # đóng context sau khi test xong
    context.close()

# fixture page dùng cho từng test UI
@pytest.fixture(scope="function")
def page(browser, request):

    # tạo browser context mới cho từng test
    context = browser.new_context(
        record_video_dir=str(VIDEOS_DIR),
        record_video_size={"width": 1280, "height": 720},
    )

    # bật tracing để debug khi cần
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    # tạo page/tab mới
    page_obj = context.new_page()

    # set timeout mặc định cho action như click/fill/goto
    page_obj.set_default_timeout(30000)

    # set timeout mặc định cho navigation như goto/load
    page_obj.set_default_navigation_timeout(60000)

    # trả page cho test chạy
    yield page_obj

    # phần teardown giữ nguyên như hiện tại