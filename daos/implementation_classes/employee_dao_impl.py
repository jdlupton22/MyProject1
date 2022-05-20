from daos.abstract_classes.employee_dao import EmployeeDao
from entities.employee import Employee
from exceptions.employee_not_found import EmployeeNotFound
from util.database_connection import connection


def _build_employee(profile):
    if profile:
        return Employee(emp_id=profile[0], email=profile[1], first_name=profile[2], last_name=profile[3],
                        title=profile[4], supervisor=profile[5], department=profile[6], dept_head=profile[7])
    else:
        return None


class EmployeeDaoImpl(EmployeeDao):
    def create_employee(self, employee):
        sql = "INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s, %s, %s) RETURNING *"

        cursor = connection.cursor()
        cursor.execute(sql, [employee.employee_id, employee.email, employee.first_name, employee.last_name,
                             employee.title, employee.supervisor, employee.department, employee.dept_head])

        connection.commit()
        profile = cursor.fetchone()

        return _build_employee(profile)

    def read_employee(self, emp_id):
        sql = "SELECT * FROM employees WHERE emp_id = %s"

        cursor = connection.cursor()
        cursor.execute(sql, [emp_id])

        profile = cursor.fetchone()

        if profile:
            return _build_employee(profile)
        else:
            raise EmployeeNotFound(f"Employee associated with id: {emp_id} - does not exist!")

    def all_employees(self):
        sql = "SELECT * FROM employees"

        cursor = connection.cursor()
        cursor.execute(sql)

        profiles = cursor.fetchall()

        employee_list = [_build_employee(profile) for profile in profiles]
        if profiles:
            return employee_list

    def update_employee(self, change):
        sql = "UPDATE employees SET emp_id = %s, email = %s, first_name = %s, last_name = %s," \
              " title = %s, supervisor = %s, department = %s, dept_head = %s WHERE emp_id = %s RETURNING *"

        cursor = connection.cursor()
        cursor.execute(sql, [change.emp_id, change.email, change.first_name, change.last_name,
                             change.title, change.supervisor, change.department, change.dept_head])

        connection.commit()
        profile = cursor.fetchone()

        return _build_employee(profile)

    def delete_employee(self, emp_id):
        sql = "DELETE FROM employees WHERE emp_id = %s"

        cursor = connection.cursor()
        cursor.execute(sql, [emp_id])
        connection.commit()


def _test():
    ed = EmployeeDaoImpl()
    employee = ed.read_employee(1001)
    print(employee)
    print("---------------------")
    print(ed.all_employees())
    # ed = EmployeeDaoImpl()
    # print(ed.delete_employee(1006))

    # employee = Employee(emp_id=1005, email="employee5@trms.com", first_name="Smitty", last_name="Voss",
    #                     title="Receptionist", supervisor=2002, department="Admin", dept_head=False)
    # employee = ed.create_employee(employee)
    # print(employee)
    # employee = Employee(emp_id=1006, email="employee6@trms.com", first_name="Byran", last_name="Pulaski",
    #                     title="Clerk", supervisor=2001, department="Admin", dept_head=False)
    # employee = ed.create_employee(employee)
    # print(employee)


if __name__ == '__main__':
    _test()
