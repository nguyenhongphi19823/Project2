# test API đầu tiên bằng Playwright
def test_get_users_api(playwright):

    # tạo API request context
    api_context = playwright.request.new_context()

    # gửi GET request
    response = api_context.get(
        "https://jsonplaceholder.typicode.com/users"
    )

    # verify status code
    assert response.status == 200

    # convert response thành JSON
    data = response.json()

    # verify response là list
    assert isinstance(data, list)

    # verify có ít nhất 1 user
    assert len(data) > 0

    # verify user đầu tiên có key name
    assert "name" in data[0]

    # đóng API context
    api_context.dispose()