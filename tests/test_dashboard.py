# test kiểm tra có thể mở dashboard bằng session đã login
def test_open_dashboard_with_saved_login(logged_in_page):

    # mở trang chính DP360
    logged_in_page.goto("https://app.dp360crm.com")

    # chờ trang load xong
    logged_in_page.wait_for_load_state("networkidle")

    # kiểm tra URL hiện tại không chứa /login
    assert "/login" not in logged_in_page.url