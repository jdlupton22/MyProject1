import enum


class AuthPriv(enum.Enum):
    EMPLOYEE = 'EMPLOYEE'
    SUPERVISOR = 'SUPERVISOR'
    BENCO = 'BENCO'
    DEPT_HEAD = 'DEPT_HEAD'
    ADMIN = 'ADMIN'

# print("All of these ENUM are related to Authorization Privileges")
# for Priv in AuthPriv:
#     print(Priv)
#
# # Hashing enum member as dictionary
# di = {AuthPriv.EMPLOYEE: 'employee', AuthPriv.SUPERVISOR: 'supervisor'}
#
# # checking if enum values are hashed successfully
# if di == {AuthPriv.EMPLOYEE: 'employee', AuthPriv.SUPERVISOR: 'supervisor'}:
#     print("Enum is hashed")
# else:
#     print("Enum is not hashed")
