import enum


class EventType(enum.Enum):
    UNIVERSITY_COURSE = 'UNIVERSITY_COURSE'
    SEMINAR = 'SEMINAR'
    CERTIFICATION_PREPARATION_CLASS = 'CERTIFICATION_PREPARATION_CLASS'
    CERTIFICATION = 'CERTIFICATION'
    TECHNICAL_TRAINING = 'TECHNICAL_TRAINING'
    OTHER = 'OTHER'


# print("All of these ENUM are related to Event Type")
# for Type in EventType:
#     print(Type)
#
# # Hashing enum member as dictionary
# di = {EventType.UNIVERSITY_COURSE: 'university_course', EventType.SEMINAR: 'seminar'}
#
# # checking if enum values are hashed successfully
# if di == {EventType.UNIVERSITY_COURSE: 'university_course', EventType.SEMINAR: 'seminar'}:
#     print("Enum is hashed")
# else:
#     print("Enum is not hashed")