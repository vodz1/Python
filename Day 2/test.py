import sqlite3

class Employee:
    employee_list = []

    def __init__(self, first_name, last_name, age, department, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.department = department
        self.salary = salary
        Employee.employee_list.append(self)
        self.insert_record_to_database()

    def insert_record_to_database(self):
        conn = sqlite3.connect('employees.db')
        c = conn.cursor()
        c.execute("INSERT INTO employee (first_name, last_name, age, department, salary) VALUES (?, ?, ?, ?, ?)",
                  (self.first_name, self.last_name, self.age, self.department, self.salary))
        conn.commit()
        conn.close()

    def transfer(self, new_department):
        self.department = new_department
        self.update_database_record()

    def update_database_record(self):
        conn = sqlite3.connect('employees.db')
        c = conn.cursor()
        c.execute("UPDATE employee SET department=? WHERE first_name=? AND last_name=?",
                  (self.department, self.first_name, self.last_name))
        conn.commit()
        conn.close()

    def fire(self):
        Employee.employee_list.remove(self)
        self.delete_record_from_database()

    def delete_record_from_database(self):
        conn = sqlite3.connect('employees.db')
        c = conn.cursor()
        c.execute("DELETE FROM employee WHERE first_name=? AND last_name=?", (self.first_name, self.last_name))
        conn.commit()
        conn.close()

    def show(self):
        print("Employee Details:")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Department: {self.department}")
        print(f"Salary: {self.salary}")

    @classmethod
    def list_employees(cls):
        print("List of Employees:")
        for employee in cls.employee_list:
            employee.show()

class Manager(Employee):
    def __init__(self, first_name, last_name, age, department, salary, managed_department):
        super().__init__(first_name, last_name, age, department, salary)
        self.managed_department = managed_department

    def show(self):
        print("Manager Details:")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Department: {self.department}")
        print("Salary: Confidential")
        print(f"Managed Department: {self.managed_department}")

def main():
    conn = sqlite3.connect('employees.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS employee
                 (first_name text, last_name text, age int, department text, salary real)''')
    conn.commit()
    conn.close()

    print("Welcome to the Employee Management System!")
    print("Options:")
    print("1. Add New Employee (Enter 'add')")
    print("2. Transfer Employee (Enter 'transfer')")
    print("3. Fire Employee (Enter 'fire')")
    print("4. List All Employees (Enter 'list')")
    print("5. Quit (Enter 'q')")

    while True:
        choice = input("Enter your choice: ").lower()
        if choice == 'add':
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            age = int(input("Enter age: "))
            department = input("Enter department: ")
            salary = float(input("Enter salary: "))
            Employee(first_name, last_name, age, department, salary)
        elif choice == 'transfer':
            first_name = input("Enter first name of employee to transfer: ")
            last_name = input("Enter last name of employee to transfer: ")
            new_department = input("Enter new department: ")
            for emp in Employee.employee_list:
                if emp.first_name == first_name and emp.last_name == last_name:
                    emp.transfer(new_department)
                    print("Employee transferred successfully!")
                    break
            else:
                print("Employee not found!")
        elif choice == 'fire':
            first_name = input("Enter first name of employee to fire: ")
            last_name = input("Enter last name of employee to fire: ")
            for emp in Employee.employee_list:
                if emp.first_name == first_name and emp.last_name == last_name:
                    emp.fire()
                    print("Employee fired successfully!")
                    break
            else:
                print("Employee not found!")
        elif choice == 'list':
            if len(Employee.employee_list) == 0:
             print("No Employees yet")
            else:
             Employee.list_employees()
        elif choice == 'q':
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
