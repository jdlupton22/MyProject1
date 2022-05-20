from daos.abstract_classes.reimbursement_status_dao import ReimbursementStatusDao
from entities.reimbursement_status import ReimbursementStatus
from exceptions.request_not_found import RequestNotFound
from util.database_connection import connection


def _build_reimbursement_status(profile):
    if profile:
        return ReimbursementStatus(request_id=profile[0], projected_award=profile[9],
                                   urgent=profile[10], status=profile[11], stage=profile[12],
                                   request_date_time=profile[13])
    else:
        return None


class ReimbursementStatusDaoImpl(ReimbursementStatusDao):

    def read_reimbursement_status(self, request_id):
        sql = "SELECT * FROM reimburse_status WHERE request_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [request_id])

        profile = cursor.fetchone()

        if profile:
            return _build_reimbursement_status(profile)
        else:
            raise RequestNotFound(f"No request with that id: {request_id} - was found!")

    def all_reimbursement_statuses(self):
        sql = "SELECT * FROM reimburse_status"
        cursor = connection.cursor()
        cursor.execute(sql)

        profiles = cursor.fetchall()
        status_list = [_build_reimbursement_status(profile) for profile in profiles]
        if profiles:
            return status_list
        else:
            raise RequestNotFound(f"No requests found!")

    def update_reimbursement_status(self, change):
        sql = "UPDATE reimburse_status SET project_award = %s, urgent = %s, status = %s, stage = %s," \
              " request_date_time = %s WHERE request_id = %s RETURNING *"
        cursor = connection.cursor()
        cursor.execute(sql, [change.projected_awards, change.urgent, change.status, change.stage,
                             change.request_date_time, change.request_id])

        connection.commit()
        profile = cursor.fetchone()
        return _build_reimbursement_status(profile)


def _test():
    rsd = ReimbursementStatusDaoImpl()
    status = rsd.read_reimbursement_status(2)
    print(status)
    print("---------------------------------")
    print(rsd.all_reimbursement_statuses())


if __name__ == '__main__':
    _test()
