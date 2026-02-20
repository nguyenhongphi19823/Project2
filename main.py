# name = "Phi"
# experience = 3
# is_automation = False
# print(name)
# print(experience)
# print(is_automation)
# print(f"I am {name} and I have {experience} years of experience")
##---------------------------------
# skills = ["manual", "api", "automation"]
# print(skills)
# print(skills[0])
# print(skills[1])
##---------------------------------
# user = {
#     "username": "phi",
#     "email": "phi@test.com",
#     "role": "tester"
# }
# print(user)
# print(user["email"])
#
##---------------------------------

lst = [
    {"email": "a@test.com", "role": "admin"},
    {"email": "b@test.com", "role": "tester"}
]
print(lst[1]["email"])

#---------------------------------

for user in lst:
    if user["role"] == "admin":
        print("Found admin:", user["email"])