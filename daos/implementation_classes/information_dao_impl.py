import datetime

from daos.abstract_classes.information_dao import InformationDao
from entities.information import Information
from exceptions.request_not_found import RequestNotFound
from util.database_connection import connection


def _build_information(profile):
    if profile:
        return Information(info_id=profile[0], related_id=profile[1], destination_id=profile[2], sender_id=profile[3],
                           sender=profile[4], urgent=profile[5], description=profile[6], request_date_time=profile[7])
    else:
        return None


class InformationDaoImpl(InformationDao):

    def create_information(self, information):
        sql = "INSERT INTO info_requests VALUES (DEFAULT, %s, %s, %s, %s, %s, %s, %s) RETURNING *"
        cursor = connection.cursor()
        cursor.execute(sql, [information.related_id, information.destination_id,
                             information.sender_id, information.sender, information.urgent, information.description,
                             information.request_date_time])

        connection.commit()
        profile = cursor.fetchone()

        return _build_information(profile)

    def read_information(self, info_id):
        sql = "SELECT * FROM info_requests WHERE info_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [info_id])

        profile = cursor.fetchone()

        if profile:
            return _build_information(profile)
        else:
            raise RequestNotFound(f"Request associated with id: {info_id} - was not found!")

    def all_informations(self):
        sql = "SELECT * FROM info_requests"
        cursor = connection.cursor()
        cursor.execute(sql)

        profiles = cursor.fetchall()
        information_list = [_build_information(profile) for profile in profiles]
        if profiles:
            return information_list
        else:
            raise RequestNotFound(f"No requests found!")

    def update_information(self, change):
        sql = "INSERT INTO info_requests VALUES (related_id = %s, destination_id = %s," \
              "sender_id = %s, sender = %s, urgent = %s, description = %s, request_date_time = %s)" \
              " WHERE info_id = %s RETURNING *"
        cursor = connection.cursor()
        cursor.execute(sql, [change.related_id, change.destination_id,
                             change.sender_id, change.sender, change.urgent, change.description,
                             change.request_date_time, change.info_id])

    def delete_information(self, info_id):
        sql = "SELECT * FROM info_requests WHERE info_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [info_id])
        connection.commit()


def _test():
    ird = InformationDaoImpl()
    information = ird.read_information(1)
    print(information)
    print("-------------------------------------------")
    information = Information(info_id=2, related_id=1, destination_id=1001, sender_id=2001, sender="super1",
                              urgent=False,
                              description="need re-enrollment verification", request_date_time=datetime.datetime)
    information = ird.create_information(information)
    print(ird.all_informations())


if __name__ == '__main__':
    _test()
