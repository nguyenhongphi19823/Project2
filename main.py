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


lst = [
    {"email": "a@test.com", "role": "admin"},
    {"email": "b@test.com", "role": "tester"}
]

def get_emails_by_role(users, role):
    emails = []
    for user in users:
        if user["role"] == role:
            emails.append(user["email"])
    return emails

result = get_emails_by_role(lst, "tester")
print(result)
