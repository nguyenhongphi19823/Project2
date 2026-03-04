# # name = "Phi"
# # experience = 3
# # is_automation = False
# # print(name)
# # print(experience)
# # print(is_automation)
# # print(f"I am {name} and I have {experience} years of experience")
# ##---------------------------------List---------
# # skills = ["manual", "api", "automation"]
# # print(skills)
# # print(skills[0])
# # print(skills[1])
# ##---------------------------------Dictionary-----------
# # user = {
# #     "username": "phi",
# #     "email": "phi@test.com",
# #     "role": "tester"
# # }
# # print(user)
# # print(user["email"])
# #
# ##---------------------------------
#
# # lst = [
# #     {"email": "a@test.com", "role": "admin"},
# #     {"email": "b@test.com", "role": "tester"}
# # ]
# #print(lst[1]["email"])
#
# #---------------------------------
# # found_admin = False
# # for user in lst:
# #     if user["role"] == "admin":
# #         print(f"Found admin:", user["email"])
# #         found_admin = True
# # if not found_admin:
# #     print("No admin found")
#
# # found_tester = False
# # for user in lst:
# #     if user["role"] == "tester":
# #         print(f"Found tester:", user["email"])
# #         found_tester = True
# #
# # if not found_tester:
# #     print(f"No tester found")
#
# # lst = [
# #     {"email": "a@test.com", "role": "admin"},
# #     {"email": "b@test.com", "role": "tester"}
# # ]
# #
# # def check_role(users, role):
# #     found = False
# #     for user in users:
# #         if user["role"] == role:
# #             print(f"Found {role}: {user["email"]}")
# #             found = True
# #
# #     if not found:
# #         print(f"No {role} found")
# #
# # check_role(lst, "admin")
# # check_role(lst, "tester")
#
#
# # lst = [
# #     {"email": "a@test.com", "role": "admin"},
# #     {"email": "b@test.com", "role": "tester"}
# # ]
#
# # def get_emails_by_role(users, role):
# #     emails = []
# #     for user in users:
# #         if user["role"] == role:
# #             emails.append(user["email"])
# #     return emails
# #
# # result = get_emails_by_role(lst, "tester")
# # assert len(result) > 0
# # print("Test passed")
#
# # def get_emails_by_role(users, role):
# #     return [user["email"] for user in users if user["role"] == role]
#
# # lst = [
# #     {"email": "a@test.com", "role": "admin"},
# #     {"email": "b@test.com", "role": "tester"}
# # ]
# #
# # def has_role(users, role):
# #     for user in users:
# #         if user["role"] == role:
# #             return True
# #
# #     return False
# #
# # assert has_role(lst, "admin") is True
# # assert has_role(lst, "manager") is False
#
#
# lst = [
#     {"email": "a@test.com", "role": "admin"},
#     {"email": "b@test.com", "role": "tester"}
# ]
#
# class UserManager:
#     def __init__(self, users):
#         self.users = users
#     def has_role(self, role):
#         for user in self.users:
#             if user["role"] == role:
#                 return True
#         return False
#     def get_emails_by_role(self, role):
#         emails = []
#         for user in self.users:
#             if user["role"] == role:
#                 emails.append(user["email"])
#         return emails
#
#     def count_users(self):
#         return len(self.users)
#
#     def add_user(self, email, role):
#         new_user = {"email": email, "role": role}
#         self.users.append(new_user)
#
#     # def remove_user_by_email(self, email):
#     #     for user in self.users:
#     #         if user["email"] == email:
#     #             self.users.remove(user)
#     #             break
#
#
#     def remove_user_by_email(self, email):
#        self.users = [
#           user for user in self.users
#              if user["email"] != email
#     ]
#
#
#
# # manager = UserManager(lst)
# # manager.add_user("c@test.com", "manager")
# # print(manager.has_role("tester"))
# # print(manager.has_role("manager"))
# # print(manager.count_users())
# # print(manager.has_role("manager"))
#
#
# manager = UserManager(lst)
# print(manager.count_users())  # 2
# manager.remove_user_by_email("a@test.com")
# print(manager.count_users())  # 1
# print(manager.has_role("admin"))  # False



# def divide(a, b):
#     try:
#         return a / b
#     except ZeroDivisionError:
#         return None

# def safe_get_email(user):
#     return user.get("email")
#     # try:
#     #     return user["email"]
#     # except KeyError:
#     #     return None
#
# print(safe_get_email({"email": "a@test.com"}))
# print(safe_get_email({"role": "tester"}))




# def get_required_email(user):
#     if "email" not in user:
#         raise Exception("User must have email")
#     return user["email"]
#
#
# print(get_required_email({"role": "admin"}))



# logging.basicConfig(level=logging.INFO)
# logging.info("Test Started")
# logging.warning("This is a warning")
# logging.error("Something went wrong")

# import logging
#
# # ✅ Logging config (ghi ra file + console)
# logging.basicConfig(
#     level=logging.INFO,
#     format="%(asctime)s - %(levelname)s - %(message)s",
#     filename="automation.log",
#     filemode="a"
# )
#
# logger = logging.getLogger(__name__)
#
# # ✅ Custom Exception
# class UserNotFoundError(Exception):
#     def __init__(self, email):
#         super().__init__(f"User with email {email} not found")
#         self.email = email
#
# # ✅ UserManager class
# class UserManager:
#     def __init__(self, users):
#         self.users = users
#
#     def get_user_by_email(self, email):
#         for user in self.users:
#             if user["email"] == email:
#                 logger.info(f"User {email} found")
#                 return user
#
#         logger.error(f"User {email} not found")
#         raise UserNotFoundError(email)
#
#     def add_user(self, email, role):
#         logger.info(f"Adding user {email}")
#         self.users.append({"email": email, "role": role})
#
# # ✅ Test data
# lst = [
#     {"email": "a@test.com", "role": "admin"},
#     {"email": "b@test.com", "role": "tester"}
# ]
#
# # ✅ Run thử
# manager = UserManager(lst)
# print(manager.get_user_by_email("a@test.com"))
# try:
#     print(manager.get_user_by_email("x@test.com"))
# except UserNotFoundError as e:
#     logger.critical(f"Exception caught: {e}")


# import json
# import logging
#
# logging.basicConfig(
#     level=logging.INFO,
#     format="%(asctime)s - %(levelname)s - %(message)s",
#     filename="automation.log",
#     filemode="a"
# )
# logger = logging.getLogger(__name__)
#
# try:
#     with open("users.json", "r") as file:
#         data = json.load(file)
# except FileNotFoundError:
#     logger.error("users.json not found")
#     raise
#
#
# class UserNotFoundError(Exception):
#     def __init__(self, email):
#         super().__init__(f"User with email {email} not found")
#         self.email = email
#
#
# class UserManager:
#     def __init__(self, users):
#         self.users = users
#
#     def get_user_by_email(self, email):
#         for user in self.users:
#             if user["email"] == email:
#                 logger.info(f"User {email} found")
#                 return user
#
#         logger.error(f"User {email} not found")
#         raise UserNotFoundError(email)
#
#     def add_user(self, email, role):
#         logger.info(f"Adding user {email}")
#         self.users.append({"email": email, "role": role})
#
#     def remove_user_by_email(self, email):
#         for user in self.users:
#             if user["email"] == email:
#                 logger.info(f"Removing user {email}")
#                 self.users.remove(user)
#                 return
#
#         logger.error(f"User {email} not found for removal")
#         raise UserNotFoundError(email)
#
#     def save_to_file(self, filename):
#         with open(filename, "w") as file:
#             json.dump(self.users, file, indent=4)
#         logger.info(f"Users saved to {filename}")
#
#
# # Run thử
# manager = UserManager(data)
#
# manager.add_user("c@test.com", "manager")
# manager.remove_user_by_email("a@test.com")
# manager.save_to_file("users.json")
#
# try:
#     manager.get_user_by_email("x@test.com")
# except UserNotFoundError as e:
#     logger.critical(f"Exception caught: {e}")


import json  # Làm việc với JSON: đọc (load) và ghi (dump) dữ liệu test/config
import logging  # Logging chuyên nghiệp thay cho print (có level, timestamp, ghi file)

# =========================
# LOGGING CONFIG
# =========================
logging.basicConfig(
    level=logging.INFO,  # Chỉ ghi log từ INFO trở lên (INFO/WARNING/ERROR/CRITICAL). DEBUG sẽ bị bỏ qua
    format="%(asctime)s - %(levelname)s - %(message)s",  # Format: thời gian - level - message
    filename="automation.log",  # Ghi log vào file automation.log (không chỉ in ra console)
    filemode="a"  # Append: chạy lần sau sẽ ghi nối tiếp, không ghi đè file cũ
)

# Tạo logger riêng cho module/file hiện tại (best practice khi project có nhiều file)
logger = logging.getLogger(__name__)

# =========================
# LOAD TEST DATA FROM JSON
# =========================
try:
    # Mở file users.json ở chế độ đọc ("r"); with giúp tự đóng file sau khi đọc xong
    with open("app/users.json", "r") as file:
        # json.load(file) chuyển JSON -> Python object
        # Nếu JSON bắt đầu bằng [ ... ] thì data sẽ là list; mỗi phần tử là dict user
        data = json.load(file)
except FileNotFoundError:
    # Nếu không có file users.json: log lỗi và dừng chương trình ngay
    # (Không có test data thì không nên chạy tiếp)
    logger.error("users.json not found")
    raise  # Ném lại lỗi gốc để fail fast

# =========================
# CUSTOM EXCEPTION
# =========================
class UserNotFoundError(Exception):
    # Custom exception dành riêng cho lỗi "không tìm thấy user"
    def __init__(self, email):
        # Gọi constructor của Exception để set message hiển thị khi raise
        super().__init__(f"User with email {email} not found")
        # Lưu email vào object exception để debug/log/report sau này
        self.email = email

# =========================
# BUSINESS LOGIC CLASS
# =========================
class UserManager:
    def __init__(self, users):
        # Lưu danh sách users vào state của object (self.users)
        self.users = users

    def get_user_by_email(self, email):
        # Duyệt toàn bộ danh sách user để tìm theo email
        for user in self.users:
            # user là dict, ví dụ {"email": "...", "role": "..."}
            if user["email"] == email:
                # Tìm thấy -> log INFO và return dict user (kết thúc hàm ngay)
                logger.info(f"User {email} found")
                return user

        # Duyệt hết không thấy -> log ERROR và raise custom exception để fail đúng nghiệp vụ
        logger.error(f"User {email} not found")
        raise UserNotFoundError(email)

    def add_user(self, email, role):
        # Log hành động trước khi thay đổi dữ liệu (giúp trace khi debug)
        logger.info(f"Adding user {email}")
        # Thêm user mới vào list; đây là thay đổi state của object
        self.users.append({"email": email, "role": role})

    def remove_user_by_email(self, email):
        # Duyệt danh sách để tìm user cần xóa
        for user in self.users:
            if user["email"] == email:
                # Tìm thấy -> log INFO và xóa user khỏi list
                logger.info(f"Removing user {email}")
                self.users.remove(user)
                return  # Xóa xong thì dừng hàm (không cần loop tiếp)

        # Không tìm thấy user để xóa -> log ERROR và raise để báo lỗi đúng nghiệp vụ
        logger.error(f"User {email} not found for removal")
        raise UserNotFoundError(email)

    def save_to_file(self, filename):
        # Ghi danh sách users hiện tại ra file JSON (ghi đè nội dung cũ)
        with open(filename, "w") as file:
            # json.dump: Python object -> JSON và ghi vào file
            # indent=4 giúp file JSON dễ đọc (pretty print)
            json.dump(self.users, file, indent=4)
        # Log sau khi lưu thành công
        logger.info(f"Users saved to {filename}")

# =========================
# DEMO RUN (MINI PROJECT)
# =========================

# Tạo object UserManager với data load từ users.json
manager = UserManager(data)

# Thử thêm user mới (sẽ log INFO)
manager.add_user("c@test.com", "manager")

# Thử xóa user có email a@test.com (nếu có sẽ log INFO; nếu không có sẽ raise)
manager.remove_user_by_email("a@test.com")

# Lưu danh sách users sau khi add/remove về lại users.json (sẽ log INFO)
manager.save_to_file("users.json")

# Thử case lỗi: tìm user không tồn tại để thấy flow ERROR -> raise -> except
try:
    manager.get_user_by_email("x@test.com")  # Không có -> log ERROR rồi raise UserNotFoundError
except UserNotFoundError as e:
    # Bắt đúng loại lỗi và log CRITICAL (mức nghiêm trọng/cần chú ý)
    logger.critical(f"Exception caught: {e}")