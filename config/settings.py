# import os để đọc biến môi trường
import os

# import load_dotenv để load dữ liệu từ file .env
from dotenv import load_dotenv


# load file .env ở root project
load_dotenv()


# lấy base URL từ .env
BASE_URL = os.getenv("DP360_BASE_URL", "https://app.dp360crm.com")

# lấy username từ .env
USERNAME = os.getenv("DP360_USERNAME")

# lấy password từ .env
PASSWORD = os.getenv("DP360_PASSWORD")

# lấy browser từ .env, nếu không có thì mặc định chromium
BROWSER = os.getenv("BROWSER", "chromium")

# lấy headless từ .env, nếu không có thì mặc định false
HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"

# timeout mặc định cho test, đơn vị millisecond
DEFAULT_TIMEOUT = int(os.getenv("DEFAULT_TIMEOUT", "30000"))