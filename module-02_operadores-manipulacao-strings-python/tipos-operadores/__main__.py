import random


# messages
USER_ALLOWED = "User allowed."
USER_NOT_ALLOWED = "User Not allowed!!!"
USER_CANT_ACCESS = "User can't access!"

# data store
users = ["mathew", "john", "luke", "paul", "marcus"]
permissions = ["create", "edit", "delete", "clone", "review"]
users_permissions = [
    {"mathew": permissions},
    {"john": [p for p in permissions if p != "delete"]},
    {"luke": [p for p in permissions if p != "delete" and p != "clone"]},
    {"paul": [permissions[-1]]},
    {"marcus": [permissions[-1]]},
]


def is_user_allowed(user, permission) -> str:
    if not user in [next(iter(p)) for p in users_permissions]:
        return USER_CANT_ACCESS

    privileges = [
        next(iter(p.values()))
        for p in users_permissions
        if user in next(iter(p.keys()))
    ][0]

    return USER_ALLOWED if permission in privileges else USER_NOT_ALLOWED


if __name__ == "__main__":
    user_logged_in = input("Type your user name: ")
    required_permission = random.choice(permissions)
    is_user_allowed = is_user_allowed(user_logged_in, required_permission)
    print(f"{required_permission}: {is_user_allowed}")
