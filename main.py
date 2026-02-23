# name = "Phi"
# experience = 3
# is_automation = False
# print(name)
# print(experience)
# print(is_automation)
# print(f"I am {name} and I have {experience} years of experience")
##---------------------------------List---------
# skills = ["manual", "api", "automation"]
# print(skills)
# print(skills[0])
# print(skills[1])
##---------------------------------Dictionary-----------
# user = {
#     "username": "phi",
#     "email": "phi@test.com",
#     "role": "tester"
# }
# print(user)
# print(user["email"])
#
##---------------------------------

# lst = [
#     {"email": "a@test.com", "role": "admin"},
#     {"email": "b@test.com", "role": "tester"}
# ]
#print(lst[1]["email"])

#---------------------------------
# found_admin = False
# for user in lst:
#     if user["role"] == "admin":
#         print(f"Found admin:", user["email"])
#         found_admin = True
# if not found_admin:
#     print("No admin found")

# found_tester = False
# for user in lst:
#     if user["role"] == "tester":
#         print(f"Found tester:", user["email"])
#         found_tester = True
#
# if not found_tester:
#     print(f"No tester found")

# lst = [
#     {"email": "a@test.com", "role": "admin"},
#     {"email": "b@test.com", "role": "tester"}
# ]
#
# def check_role(users, role):
#     found = False
#     for user in users:
#         if user["role"] == role:
#             print(f"Found {role}: {user["email"]}")
#             found = True
#
#     if not found:
#         print(f"No {role} found")
#
# check_role(lst, "admin")
# check_role(lst, "tester")


# lst = [
#     {"email": "a@test.com", "role": "admin"},
#     {"email": "b@test.com", "role": "tester"}
# ]

# def get_emails_by_role(users, role):
#     emails = []
#     for user in users:
#         if user["role"] == role:
#             emails.append(user["email"])
#     return emails
#
# result = get_emails_by_role(lst, "tester")
# assert len(result) > 0
# print("Test passed")

# def get_emails_by_role(users, role):
#     return [user["email"] for user in users if user["role"] == role]

# lst = [
#     {"email": "a@test.com", "role": "admin"},
#     {"email": "b@test.com", "role": "tester"}
# ]
#
# def has_role(users, role):
#     for user in users:
#         if user["role"] == role:
#             return True
#
#     return False
#
# assert has_role(lst, "admin") is True
# assert has_role(lst, "manager") is False


lst = [
    {"email": "a@test.com", "role": "admin"},
    {"email": "b@test.com", "role": "tester"}
]

class UserManager:
    def __init__(self, users):
        self.users = users
    def has_role(self, role):
        for user in self.users:
            if user["role"] == role:
                return True
        return False
    def get_emails_by_role(self, role):
        emails = []
        for user in self.users:
            if user["role"] == role:
                emails.append(user["email"])
        return emails

    def count_users(self):
        return len(self.users)

    def add_user(self, email, role):
        new_user = {"email": email, "role": role}
        self.users.append(new_user)


manager = UserManager(lst)
manager.add_user("c@test.com", "manager")
print(manager.has_role("tester"))
print(manager.has_role("manager"))
print(manager.count_users())
print(manager.has_role("manager"))



