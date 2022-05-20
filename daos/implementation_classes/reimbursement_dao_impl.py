from daos.abstract_classes.reimbursement_dao import ReimbursementDao
from entities.reimbursement import Reimbursement
from exceptions.request_not_found import RequestNotFound
from util.database_connection import connection


def _build_reimbursement(profile):
    if profile:
        return Reimbursement(request_id=profile[0], emp_id=profile[1], ev_location=profile[2], ev_cost=profile[3],
                             ev_type=profile[4], description=profile[5], justification=profile[6],
                             grading_format=profile[7], grade=profile[8])
    else:
        return None


class ReimbursementDaoImpl(ReimbursementDao):

    def create_reimbursement(self, reimbursement):
        sql = "INSERT INTO reimbursements VALUES (DEFAULT, %s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING *"

        cursor = connection.cursor()
        cursor.execute(sql, [reimbursement.emp_id, reimbursement.ev_location,
                             reimbursement.ev_cost, reimbursement.ev_type, reimbursement.description,
                             reimbursement.justification, reimbursement.grading_format, reimbursement.grade])

        connection.commit()
        profile = cursor.fetchone()

        return _build_reimbursement(profile)

    def read_reimbursement(self, request_id):
        sql = "SELECT * FROM reimbursements WHERE request_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [request_id])

        profile = cursor.fetchone()

        if profile:
            return _build_reimbursement(profile)
        else:
            raise RequestNotFound(f"No request with that id: {request_id} - was found!")

    def all_reimbursements(self):
        sql = "SELECT * FROM reimbursements"
        cursor = connection.cursor()
        cursor.execute(sql)

        profiles = cursor.fetchall()
        reimbursement_list = [_build_reimbursement(profile) for profile in profiles]
        if profiles:
            return reimbursement_list

    def update_reimbursement(self, change):
        sql = "UPDATE reimbursements SET emp_id = %s, ev_location = %s, ev_cost = %s," \
              " ev_type = %s, description = %s, justification = %s, grading_format = %s, grade = %s)" \
              "WHERE request_id = %s RETURNING *"
        cursor = connection.cursor()
        cursor.execute(sql, [change.emp_id, change.ev_location, change.ev_cost, change.ev_type,
                             change.description, change.justification, change.grading_format, change.grade,
                             change.request_id])

        connection.commit()
        profile = cursor.fetchone()
        return _build_reimbursement(profile)

    def delete_reimbursement(self, request_id):
        sql = "DELETE FROM reimbursements WHERE request_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [request_id])

        profiles = cursor.fetchall()
        request_list = [_build_reimbursement(profile) for profile in profiles]
        return request_list


def _test():
    rd = ReimbursementDaoImpl()
    reimbursement = rd.read_reimbursement(1)
    print(reimbursement)
    print("------------------------------")
    print(rd.all_reimbursements())


if __name__ == '__main__':
    _test()
