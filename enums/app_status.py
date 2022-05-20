import enum


class AppStatus(enum.Enum):
    PENDING = 'PENDING'
    APPROVED = 'APPROVED'
    DENIED = 'DENIED'
    CANCELLED = 'CANCELLED'

# print("All of these ENUM are related to Application Status")
# for Status in AppStatus:
#     print(Status)
#
# # Hashing enum member as dictionary
# di = {AppStatus.PENDING: 'pending', AppStatus.APPROVED: 'approved'}
#
# # checking if enum values are hashed successfully
# if di == {AppStatus.PENDING: 'pending', AppStatus.APPROVED: 'approved'}:
#     print("Enum is hashed")
# else:
#     print("Enum is not hashed")
