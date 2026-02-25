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
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info("User created")
logger.error("Login failed")

lst = [
    {"email": "a@test.com", "role": "admin"},
    {"email": "b@test.com", "role": "tester"}
]
class UserNotFoundError(Exception):
    pass

class UserManager:
    def __init__(self, users):
        self.users = users
    def get_user_by_email(self, email):
        for user in self.users:
            if user["email"] == email:
                return user
        logger.error(f"User {email} not found")
        raise UserNotFoundError(email)

    def add_user(self, email, role):
        logger.info(f"Adding user {email}")
        self.users.append({"email": email, "role": role})

manager = UserManager(lst)
print(manager.get_user_by_email("a@test.com"))
print(manager.get_user_by_email("x@test.com"))


