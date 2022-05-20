import enum


class AppStage(enum.Enum):
    UPLOAD = "UPLOAD"
    SUPERVISOR = 'SUPERVISOR'
    DEPT_HEAD = 'DEPT_HEAD'
    BENCO = 'BENCO'
    EVENT = 'EVENT'
    END = 'END'


# print("All of these ENUM are related to Application Stages")
# for Stage in AppStage:
#     print(Stage)
#
# # Hashing enum member as dictionary
# di = {AppStage.UPLOAD: 'upload', AppStage.SUPERVISOR: 'supervisor'}
#
# # checking if enum values are hashed successfully
# if di == {AppStage.UPLOAD: 'upload', AppStage.SUPERVISOR: 'supervisor'}:
#     print("Enum is hashed")
# else:
#     print("Enum is not hashed")
