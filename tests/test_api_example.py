# import thư viện json để parse dữ liệu JSON từ API
import json

# import ProxyHandler và build_opener để tạo HTTP client bỏ qua proxy hệ thống
from urllib.request import ProxyHandler, build_opener


# hàm test kiểm tra API lấy danh sách users
def test_get_users_api():
    # tạo opener không dùng proxy để tránh lỗi môi trường local
    opener = build_opener(ProxyHandler({}))

    # gọi API lấy danh sách users với timeout 10 giây
    with opener.open("https://jsonplaceholder.typicode.com/users", timeout=10) as response:
        # kiểm tra HTTP status trả về là 200 OK
        assert response.status == 200

        # đọc response và chuyển JSON thành object Python
        data = json.load(response)

    # kiểm tra dữ liệu trả về là kiểu list
    assert isinstance(data, list)

    # kiểm tra list có ít nhất 1 phần tử
    assert len(data) > 0

    # kiểm tra phần tử đầu tiên có field name
    assert "name" in data[0]

# -------------

# import json để convert Python dict thành JSON và parse JSON response
import json

# import Request để tạo HTTP request có method POST và headers
from urllib.request import Request

# import ProxyHandler và build_opener để tạo HTTP client bỏ qua proxy hệ thống
from urllib.request import ProxyHandler, build_opener


# hàm test kiểm tra API create user
def test_create_user_api():

    # tạo opener không dùng proxy để tránh lỗi môi trường local
    opener = build_opener(ProxyHandler({}))

    # tạo payload dạng Python dict để gửi lên API
    payload = {
        # field name của user mới
        "name": "Phi",

        # field email của user mới
        "email": "phi@test.com"
    }

    # convert payload từ Python dict sang JSON string, rồi encode thành bytes
    request_body = json.dumps(payload).encode("utf-8")

    # tạo request object cho API create user
    request = Request(
        # URL API create user
        "https://jsonplaceholder.typicode.com/users",

        # data là body gửi lên API
        data=request_body,

        # method POST để tạo dữ liệu mới
        method="POST",

        # headers báo cho server biết body là JSON
        headers={
            # Content-Type cho biết request body là JSON
            "Content-Type": "application/json"
        }
    )

    # gửi request với timeout 10 giây
    with opener.open(request, timeout=10) as response:

        # kiểm tra HTTP status trả về là 201 Created
        assert response.status == 201

        # đọc response JSON và chuyển thành Python object
        response_data = json.load(response)

    # kiểm tra response trả về đúng name đã gửi
    assert response_data["name"] == "Phi"

    # kiểm tra response trả về đúng email đã gửi
    assert response_data["email"] == "phi@test.com"

    # kiểm tra response có field id do API tự tạo
    assert "id" in response_data



#-------
# test API dùng fixture
def test_get_users(api_context):

    # gửi GET request
    response = api_context.get(

        "https://jsonplaceholder.typicode.com/users"
    )

    # verify status
    assert response.status == 200
