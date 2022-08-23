#Assignment 2

from abstract_railway_employee import AbstractRailwayEmployee


class RailwayManager:
    """Railway Manager class"""
    #Constructor: employees(list of AbstractRailwayEmployee)
    def __init__(self):
        #list of employees and their IDs(int)
        self._employees = []
        self._next_available_id = 1

    #Add employee(employee: AbstractRailwayEmployee)
    def add_employee(self, employee):
        """Add a new employee to the list of employees"""
        #Assign the next available ID to the employee
        #Increment the next available ID 
        #Modify the method to return the ID of a successfully added employee
        for e in self._employees:
            if e.get_employee_id() == employee.get_employee_id():
                raise ValueError("Employee already exists")
        self._employees.append(employee)
        employee.set_id(self._next_available_id)
        self._next_available_id += 1
        return employee.get_employee_id()

        #Remove employee by ID(employee_id: int)
    def remove_employee(self, employee_id):
        """Remove an employee from the list of employees"""
        for e in self._employees:
            if e.get_employee_id() == employee_id:
                self._employees.remove(e)
                return True
        #If the employee does not exist, raise an error
        if not self.employee_exists(employee_id):
            raise ValueError("Employee does not exist")
        return False

    # get(id : int) : AbstractEmployee
    def get_employee(self, employee_id):
        """Get an employee from the list of employees"""
        for e in self._employees:
            if e.get_employee_id() == employee_id:
                return e
        #If the employee does not exist, raise an error
        if not self.employee_exists(employee_id):
            raise ValueError("Employee does not exist")
        return None


    # employee_exists(id : int) : bool
    def employee_exists(self, employee_id):
        """Check if an employee exists in the list of employees"""
        for e in self._employees:
            if e.get_employee_id() == employee_id:
                return True
        return False

    #get_all_employees() : list of AbstractRailwayEmployee
    def get_all_employees(self):
        """Get all employees from the list of employees"""
        return self._employees

    # get_all_by_type(type : string) : AbstractEmployee[]
    def get_all_by_type(self, type):
        """Get all employees of a certain type from the list of employees"""
        employees = []
        for e in self._employees:
            if e.get_type() == type:
                employees.append(e)
        return employees
        
 
    
    # update(employee : AbstractEmployee)
    def update_employee(self, employee):
        """Update an employee in the list of employees"""
        #If the employee does not exist, raise an error
        if not self.employee_exists(employee.get_employee_id()):
            raise ValueError("Employee does not exist")
        for e in self._employees:
            if e.get_employee_id() == employee.get_employee_id():
                self._employees.remove(e)
                self._employees.append(employee)
                return True
        return False