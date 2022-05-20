class Employee(object):
    def __init__(self, emp_id: int, email: str, first_name: str, last_name: str, title: str, supervisor: int,
                 department: str, dept_head: bool):
        self.emp_id = int(emp_id)
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.title = title
        self.supervisor = int(supervisor)
        self.department = department
        self.dept_head = bool(dept_head)

    def __repr__(self):
        return str({
            "emp_id": self.emp_id,
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "title": self.title,
            "supervisor": self.supervisor,
            "department": self.department,
            "dept_head": self.dept_head

        })

    def json(self):
        return {
            "empId": self.emp_id,
            "email": self.email,
            "firstName": self.first_name,
            "lastName": self.last_name,
            "title": self.title,
            "supervisor": self.supervisor,
            "department": self.department,
            "deptHead": self.dept_head

        }
