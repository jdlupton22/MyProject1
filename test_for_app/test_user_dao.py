from entities.user import User
from data_access_layer.implementation_classes.user_dao_imp import UserDAOImp

user_test = User(0, "Hashlib testing here", "Jeremiah", "Lupton", True)
user_update_test = User(3, "Updated hashlib testing", "Jeremiah", "Lupton", False)
user_dao = UserDAOImp()


def test_dao_create_user():
    new_user_in_db = user_dao.create_user_dao(user_test)
    assert new_user_in_db.user_id != 0


def test_dao_get_user():
    return_user = user_dao.get_user_dao(1)
    assert return_user.user_id != 0


def test_dao_update_user():
    return_user = user_dao.update_user_dao(user_update_test)
    assert return_user.hashed_user == "Updated hashlib testing"


def test_dao_delete_user():
    returned_bol = user_dao.delete_user_dao(3)
    assert returned_bol
