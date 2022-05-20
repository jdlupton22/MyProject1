from enums.auth_priv import AuthPriv


class Userbase(object):
    def __init__(self, user_id: int, emp_id: int, username: str, user_password: str, privilege: AuthPriv,
                 user_role: str):
        self.user_id = int(user_id)
        self.emp_id = int(emp_id)
        self.username = username
        self.user_password = user_password
        self.privilege = privilege
        self.user_role = user_role

    def __repr__(self):
        return str({
            "user_id": self.user_id,
            "emp_id": self.emp_id,
            "username": self.username,
            "user_password": self.user_password,
            "privilege": self.privilege,
            "user_role": self.user_role
        })

    def json(self):
        return {
            "userId": self.user_id,
            "empId": self.emp_id,
            "username": self.username,
            "userPassword": self.user_password,
            "privilege": self.privilege,
            "user_role": self.user_role
        }