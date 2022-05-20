from daos.abstract_classes.userbase_dao import UserbaseDao


class UserbaseServiceImpl:
    def __init__(self, userbase_dao: UserbaseDao):
        self.userbase_dao = userbase_dao

    def service_validate_userbase(self, username, user_password, user_role):
        return self.userbase_dao.login_userbase(username, user_password, user_role)

    def service_create_userbase(self, userbase):
        return self.userbase_dao.create_userbase(userbase)

    def service_read_userbase(self, user_id):
        return self.userbase_dao.read_userbase(user_id)

    def service_all_userbases(self):
        return self.userbase_dao.all_userbases()

    def service_update_userbase(self, change):
        return self.userbase_dao.update_userbase(change)

    def service_delete_userbase(self, user_id):
        return self.userbase_dao.delete_userbase(user_id)
