from daos.abstract_classes.userbase_dao import UserbaseDao
from entities.userbase import Userbase
from exceptions.user_not_found import UserNotFound
from util.database_connection import connection


def _build_userbase(profile):
    if profile:
        return Userbase(user_id=profile[0], emp_id=profile[1], username=profile[2], user_password=profile[3],
                        privilege=profile[4], user_role=profile[5])
    else:
        return None


class UserbaseDaoImpl(UserbaseDao):

    def create_userbase(self, userbase):
        sql = "INSERT INTO userbase VALUES (DEFAULT, %s, %s, %s, %s, %s) RETURNING *"

        cursor = connection.cursor()
        cursor.execute(sql, [userbase.emp_id, userbase.username, userbase.user_password, userbase.privilege,
                             userbase.user_role])

        connection.commit()
        profile = cursor.fetchone()

        return _build_userbase(profile)

    def read_userbase(self, user_id):
        sql = "SELECT * FROM userbase WHERE user_id = %s"

        cursor = connection.cursor()
        cursor.execute(sql, [user_id])

        profile = cursor.fetchone()

        if profile:
            return _build_userbase(profile)
        else:
            raise UserNotFound(f"User associated with id: {user_id} - does not exist!")

    def all_userbases(self):
        sql = "SELECT * FROM userbase"

        cursor = connection.cursor()
        cursor.execute(sql)

        profiles = cursor.fetchall()
        userbase_list = [_build_userbase(profile) for profile in profiles]

        if profiles:
            return userbase_list
        else:
            raise UserNotFound(f"No users found!")

    def update_userbase(self, change):
        sql = "UPDATE userbase SET emp_id = %s, username = %s, user_password = %s, privilege = %s, user_role = %s)" \
              " WHERE user_id = %s RETURNING *"

        cursor = connection.cursor()
        cursor.execute(sql, [change.emp_id, change.username, change.user_password, change.privilege, change.user_role,
                             change.user_id])

        connection.commit()
        profile = cursor.fetchone()

        return _build_userbase(profile)

    def delete_userbase(self, user_id):
        sql = "DELETE FROM userbase WHERE user_id = %s"

        cursor = connection.cursor()
        cursor.execute(sql, [user_id])
        connection.commit()

    def login_userbase(self, username, user_password, user_role):
        sql = "SELECT * FROM userbase WHERE username = %s AND user_password = %s AND user_role"
        cursor = connection.cursor()
        cursor.execute(sql, [username, user_password, user_role])

        connection.commit()
        profile = cursor.fetchone()

        return _build_userbase(profile)


def _test():
    ubd = UserbaseDaoImpl()
    userbase = ubd.read_userbase(101)
    print(userbase)

    # userbase = Userbase(user_id=9, emp_id=1005, username="employee5", user_password="Password5*",
    #                     privilege=AuthPriv.EMPLOYEE)
    # userbase = ubd.create_userbase(userbase)
    # print(userbase)


if __name__ == '__main__':
    _test()
