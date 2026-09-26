#Employee Management System - OOP Project

class Employee:

    def __init__(self, name="Unknown", age=0, employee_id="NA", salary=0):
        self.name = name
        self.age = age

        self.__employee_id = employee_id
        self.__salary = salary

    def get_employee_id(self):
        return self.__employee_id

    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary

    def display(self):
        print("\nEmployee Details:")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.__employee_id)
        print("Salary: $", self.__salary)

    def __del__(self):
        print("Employee object destroyed.")


class Manager(Employee):

    def __init__(self, name, age, employee_id, salary, department):
        super().__init__(name, age, employee_id, salary)
        self.department = department

    def display(self):
        print("\nManager Details:")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.get_employee_id())
        print("Salary: $", self.get_salary())
        print("Department:", self.department)


class Developer(Employee):

    def __init__(self, name, age, employee_id, salary, programming_language):
        super().__init__(name, age, employee_id, salary)
        self.programming_language = programming_language

    def display(self):
        print("\nDeveloper Details:")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.get_employee_id())
        print("Salary: $", self.get_salary())
        print("Programming Language:", self.programming_language)


person = None
employee = None
manager = None

while True:

    print("\n--- Python OOP Project: Employee Management System ---")

    print("\nChoose an operation:")
    print("1. Create a Person")
    print("2. Create an Employee")
    print("3. Create a Manager")
    print("4. Show Details")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":

        name = input("Enter Name: ")
        age = int(input("Enter Age: "))

        person = Employee(name, age)

        print("\nPerson created with name:",
              name, "and age:", age)

    elif choice == "2":

        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        employee_id = input("Enter Employee ID: ")
        salary = float(input("Enter Salary: "))

        employee = Employee(
            name,
            age,
            employee_id,
            salary
        )

        print("\nEmployee created with name:",
              name,
              ", age:", age,
              ", ID:", employee_id,
              ", and salary: $", salary)

    elif choice == "3":

        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        employee_id = input("Enter Employee ID: ")
        salary = float(input("Enter Salary: "))
        department = input("Enter Department: ")

        manager = Manager(
            name,
            age,
            employee_id,
            salary,
            department
        )

        print("\nManager created with name:",
              name,
              ", age:", age,
              ", ID:", employee_id,
              ", salary: $", salary,
              ", and department:", department)

    elif choice == "4":

        print("\nChoose details to show:")
        print("1. Person")
        print("2. Employee")
        print("3. Manager")

        detail_choice = input("Enter your choice: ")

        if detail_choice == "1":
            if person:
                person.display()
            else:
                print("Person not created.")

        elif detail_choice == "2":
            if employee:
                employee.display()
            else:
                print("Employee not created.")

        elif detail_choice == "3":
            if manager:
                manager.display()
            else:
                print("Manager not created.")

        else:
            print("Invalid choice.")

    elif choice == "5":

        print("\nExiting the system.")
        print("All resources have been freed.")
        print("Goodbye!")

        break

    else:
        print("Invalid choice. Please try again.")