from abc import ABC, abstractmethod


class EmployeeService(ABC):
    @abstractmethod
    def service_create_employee(self, employee):
        pass

    @abstractmethod
    def service_read_employee(self, emp_id):
        pass

    @abstractmethod
    def service_all_employees(self):
        pass

    @abstractmethod
    def service_update_employee(self, change):
        pass

    @abstractmethod
    def service_delete_employee(self, emp_id):
        pass
