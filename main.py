import logging

from flask_cors import CORS
from daos.implementation_classes.attachment_dao_impl import AttachmentDaoImpl
from entities.attachment import Attachment
from exceptions.no_attachments_found import NoAttachmentsFound
from services.implementation_classes.attachment_service_impl import AttachmentServiceImpl
from daos.implementation_classes.employee_dao_impl import EmployeeDaoImpl
from entities.employee import Employee
from exceptions.employee_not_found import EmployeeNotFound
from services.implementation_classes.employee_service_impl import EmployeeServiceImpl
from daos.implementation_classes.information_dao_impl import InformationDaoImpl
from entities.information import Information
from services.implementation_classes.information_service_impl import InformationServiceImpl
from daos.implementation_classes.reimbursement_dao_impl import ReimbursementDaoImpl
from entities.reimbursement import Reimbursement
from services.implementation_classes.reimbursement_service_impl import ReimbursementServiceImpl
from daos.implementation_classes.reimbursement_status_dao_impl import ReimbursementStatusDaoImpl
from entities.reimbursement_status import ReimbursementStatus
from exceptions.resource_not_found import ResourceNotFound
from services.implementation_classes.reimbursement_status_service_impl import ReimbursementStatusServiceImpl
from daos.implementation_classes.userbase_dao_impl import UserbaseDaoImpl
from entities.userbase import Userbase
from exceptions.invalid_input_type import InvalidInputType
from exceptions.user_not_found import UserNotFound
from services.implementation_classes.userbase_service_impl import UserbaseServiceImpl
from flask import Flask, jsonify, request


ad = AttachmentDaoImpl()
asi = AttachmentServiceImpl(ad)

ed = EmployeeDaoImpl()
es = EmployeeServiceImpl(ed)

ird = InformationDaoImpl()
isi = InformationServiceImpl(ird)

rd = ReimbursementDaoImpl()
rs = ReimbursementServiceImpl(rd)

rsd = ReimbursementStatusDaoImpl()
rss = ReimbursementStatusServiceImpl(rsd)

ud = UserbaseDaoImpl()
us = UserbaseServiceImpl(ud)

logging.basicConfig(filename="records.log", level=logging.DEBUG, format=f"%(asctime)s %(levelname)s %(message)s")

app = Flask(__name__)
CORS(app)


@app.get("/attachments")
async def get_all_attachments():
    return jsonify([attachment.json() for attachment in asi.service_all_attachments()])


@app.get("/attachment/<attach_id>")
async def get_attachment(attach_id):
    try:
        return asi.service_read_attachment(int(attach_id)).json(), 200
    except InvalidInputType as i:
        return i.message, 400
    except NoAttachmentsFound as a:
        return a.message, 404


@app.post("/attachment/upload/<attach_id>")
async def post_attachment(attach_id):
    body = request.json

    attachment = Attachment(attach_id=attach_id, request_id=body["request_id"], file_type=body["file_type"],
                            file=body["file"])
    attachment = asi.service_create_attachment(attachment)

    return attachment.json()


@app.put("/attachment/update/<attach_id>")
async def put_attachment(attach_id):
    body = request.json

    attachment = Attachment(attach_id=attach_id, request_id=body["request_id"], file_type=body["file_type"],
                            file=body["file"])
    attachment = asi.service_update_attachment(attachment)

    return attachment.json()


@app.delete("/attachment/delete/<attach_id>")
async def delete_attachment(attach_id):
    asi.service_delete_attachment(attach_id)
    return "Successful Deletion", 204


# ------------------------EMPLOYEE CONTROLS----------------------------#
@app.get("/employees")
async def get_all_employees():
    return jsonify([employee.json() for employee in es.service_all_employees()])


@app.get("/employee/<emp_id>")
async def get_employee(emp_id):
    try:
        return es.service_read_employee(int(emp_id)).json(), 200
    except InvalidInputType as i:
        return i.message, 400
    except EmployeeNotFound as e:
        return e.message, 404


@app.post("/employee/create")
async def post_employee():
    body = request.json

    employee = Employee(emp_id=body["emp_id"], email=body["email"], first_name=body["first_name"],
                        last_name=body["last_name"], title=body["title"], supervisor=body["supervisor"],
                        department=body["department"], dept_head=body["dept_head"])
    employee = es.service_create_employee(employee)

    return employee.json()


@app.put("/employee/update/<emp_id>")
async def put_employee(emp_id):
    body = request.json

    employee = Employee(emp_id=emp_id, email=body["email"], first_name=body["first_name"],
                        last_name=body["last_name"], title=body["title"], supervisor=body["supervisor"],
                        department=body["department"], dept_head=body["dept_head"])
    employee = es.service_update_employee(employee)

    return employee.json()


@app.delete("/employee/delete/<emp_id>")
async def delete_employee(emp_id):
    es.service_delete_employee(emp_id)
    return "Successful Deletion", 204


# ----------------------INFORMATION CONTROLS----------------------------#
@app.get("/informations")
async def get_all_informations():
    return jsonify([information.json() for information in isi.service_all_informations()])


@app.get("/information/<info_id>")
async def get_information(info_id):
    try:
        return isi.service_read_information(int(info_id)).json(), 200
    except InvalidInputType as i:
        return i.message, 400
    except ResourceNotFound as e:
        return e.message, 404


@app.post("/information/create")
async def post_information():
    body = request.json

    information = Information(info_id=body["info_id"], related_id=body["related_id"],
                              destination_id=body["destination_id"],
                              sender_id=body["sender_id"], sender=body["sender"], urgent=body["urgent"],
                              description=body["description"], request_date_time=body["request_date_time"])
    information = isi.service_create_information(information)

    return information.json()


@app.put("/information/update/<info_id>")
async def put_information(info_id):
    body = request.json

    information = Information(info_id=info_id, related_id=body["related_id"], destination_id=body["destination_id"],
                              sender_id=body["sender_id"], sender=body["sender"], urgent=body["urgent"],
                              description=body["description"], request_date_time=body["request_date_time"])
    information = isi.service_update_information(information)

    return information.json()


@app.delete("/information/delete/<info_id>")
async def delete_information(info_id):
    isi.service_delete_information(info_id)
    return "Successful Deletion", 204


# ---------------------REIMBURSEMENT CONTROLS---------------------------#
@app.get("/reimbursements")
async def get_all_reimbursements():
    return jsonify([reimbursement.json() for reimbursement in rs.service_all_reimbursements()])


@app.get("/reimbursement/<request_id>")
async def get_reimbursement(request_id):
    try:
        return rs.service_read_reimbursement(int(request_id)).json(), 200
    except InvalidInputType as i:
        return i.message, 400
    except ResourceNotFound as e:
        return e.message, 404


@app.post("/reimbursement/create")
async def post_reimbursement():
    body = request.json

    reimbursement = Reimbursement(request_id=body["request_id"], emp_id=body["emp_id"],
                                  ev_location=body["ev_location"], ev_cost=body["ev_cost_id"],
                                  ev_type=body["ev_type"], description=body["description"],
                                  justification=body["justification"], grading_format=body["grading_format"],
                                  grade=body["grade"])
    reimbursement = rs.service_create_reimbursement(reimbursement)

    return reimbursement.json()


@app.put("/reimbursement/update/<request_id>")
async def put_reimbursement(request_id):
    body = request.json

    reimbursement = Reimbursement(request_id=request_id, emp_id=body["emp_id"],
                                  ev_location=body["ev_location"], ev_cost=body["ev_cost_id"],
                                  ev_type=body["ev_type"], description=body["description"],
                                  justification=body["justification"], grading_format=body["grading_format"],
                                  grade=body["grade"])
    reimbursement = rs.service_update_reimbursement(reimbursement)

    return reimbursement.json()


@app.delete("/reimbursement/delete/<request_id>")
async def delete_reimbursement(request_id):
    rs.service_delete_reimbursement(request_id)
    return "Successful Deletion", 204


# ---------------------REIMBURSEMENT STATUS CONTROLS---------------------#
@app.get("/statuses")
async def get_all_reimbursement_statuses():
    return jsonify([reimbursement_status.json() for reimbursement_status
                    in rss.service_all_reimbursement_statuses()])


@app.get("/status/<request_id>")
async def get_reimbursement_status(request_id):
    try:
        return rss.service_read_reimbursement_status(int(request_id)).json(), 200
    except InvalidInputType as i:
        return i.message, 400
    except ResourceNotFound as e:
        return e.message, 404


@app.put("/status/update/<request_id>")
async def put_reimbursement_status(request_id):
    body = request.json

    status = ReimbursementStatus(request_id=request_id, projected_award=body["projected_award"],
                                 urgent=body["urgent"], status=body["status"], stage=body["stage"],
                                 request_date_time=body["request_date_time"])
    status = rss.service_update_reimbursement_status(status)

    return status.json()


# ------------------------USERBASE CONTROLS------------------------------#
@app.get("/userbases")
async def get_all_userbases():
    return jsonify([userbase.json() for userbase in us.service_all_userbases()])


@app.get("/userbase/<user_id>")
async def get_userbase(user_id):
    try:
        return us.service_read_userbase(int(user_id)).json(), 200
    except InvalidInputType as i:
        return i.message, 400
    except UserNotFound as u:
        return u.message, 404


@app.post("/userbase/create")
async def post_userbase():
    body = request.json

    userbase = Userbase(user_id=body["user_id"], emp_id=body["emp_id"], username=body["username"],
                        user_password=body["user_password"], privilege=body["privilege"], user_role=body["user_role"])
    userbase = us.service_create_userbase(userbase)

    return userbase.json()


@app.put("/userbase/update/<user_id>")
async def put_userbase(user_id):
    body = request.json

    userbase = Userbase(user_id=user_id, emp_id=body["emp_id"], username=body["username"],
                        user_password=body["user_password"], privilege=body["privilege"], user_role=body["user_role"])
    userbase = us.service_update_userbase(userbase)

    return userbase.json()


@app.delete("/userbase/delete/<user_id>")
async def delete_userbase(user_id):
    us.service_delete_userbase(user_id)
    return "Successful Deletion", 204


if __name__ == '__main__':
    app.run()