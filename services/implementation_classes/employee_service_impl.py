from daos.abstract_classes.employee_dao import EmployeeDao
from services.abstract_classes.employee_service import EmployeeService


class EmployeeServiceImpl(EmployeeService):

    def __init__(self, employee_dao: EmployeeDao):
        self.employee_dao = employee_dao

    def service_create_employee(self, employee):
        return self.employee_dao.create_employee(employee)

    def service_read_employee(self, emp_id):
        return self.employee_dao.read_employee(emp_id)

    def service_all_employees(self):
        return self.employee_dao.all_employees()

    def service_update_employee(self, change):
        return self.employee_dao.update_employee(change)

    def service_delete_employee(self, emp_id):
        return self.employee_dao.delete_employee(emp_id)
