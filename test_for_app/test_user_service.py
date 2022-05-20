from custom_exceptions.custom_exception_message import CustomExceptionMessage
from service_layer.implementation_classes.user_service import UserService
from data_access_layer.implementation_classes.user_dao_imp import UserDAOImp

userDao = UserDAOImp()
UserServices = UserService(userDao)


def test_service_validate_user():
    got_user = UserServices.service_validate_user("super1", "sPassword1")
    assert got_user.user_id != 0


def test_service_create_user():
    created_user = UserServices.service_create_user("Testing", "testing", "testing", "testing", False)
    assert created_user.user_id != 0


def test_service_update_user():
    try:
        UserServices.service_update_user(0, "testing", "testing", "testing", "testing", False)

    except CustomExceptionMessage as e:
        assert str(e) == "No user associated with that id found!"
