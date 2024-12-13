# The Course class represents a course with a unique ID, name, and fee.
class Course:
    def __init__(self, course_id, name, fee):
        self.course_id = course_id
        self.name = name
        self.fee = fee

# The Student class represents a student with an ID, name, email, enrolled courses, and balance.
class Student:
    def __init__(self, student_id, name, email):
        # Initialize a Student object.
        self.student_id = student_id
        self.name = name
        self.email = email
        self.courses = [] # List to hold enrolled courses.
        self.balance = 0 # List to hold enrolled courses.

    def enroll(self, course): # Enroll the student in a course and update the balance.
        if course in self.courses:
            raise ValueError(f"{self.name} is already enrolled in {course.name}.") # throws an error If the student is already enrolled in the course.
        self.courses.append(course)
        self.balance += course.fee

    def get_total_fee(self): #Calculate the total fees for all enrolled courses snd return: Total fees as a sum of course fees.
        return sum(course.fee for course in self.courses)

# The RegistrationSystem class manages courses and students, providing various utilities.
class RegistrationSystem:
    def __init__(self): # Initialize the RegistrationSystem.
        self.courses = [] # List of available courses.
        self.students = {} # Dictionary of students, keyed by student_id.

    def add_course(self, course_id, name, fee): # Add a new course to the system.
        if any(course.course_id == course_id for course in self.courses):
            raise ValueError(f"Course with ID {course_id} already exists.") # Throws an error If a course with the same ID already exists.
        self.courses.append(Course(course_id, name, fee))
        print(f"Course '{name}' added successfully!")

    def register_student(self, student_id, name, email): # Register a new student in the system
        if student_id in self.students:
            raise ValueError(f"Student with ID {student_id} is already registered.") # throws an error if  If a student with the same ID is already registered.
        self.students[student_id] = Student(student_id, name, email)
        print(f"Student '{name}' registered successfully!")

    def enroll_in_course(self, student_id, course_id): # Enroll a student in a course.
        if student_id not in self.students:
            raise ValueError(f"Student with ID {student_id} not found.")
        student = self.students[student_id]
        course = next((course for course in self.courses if course.course_id == course_id), None)
        if not course:
            raise ValueError(f"Course with ID {course_id} not found.")
        student.enroll(course)
        print(f"Student '{student.name}' enrolled in course '{course.name}'.")

    def calculate_payment(self, student_id, amount): #  Process a payment for a student's balance.
        if student_id not in self.students:
            raise ValueError(f"Student with ID {student_id} not found.")
        student = self.students[student_id]
        if amount < 0.4 * student.balance:
            raise ValueError("Minimum payment is 40% of the outstanding balance.")
        student.balance -= amount
        print(f"Payment of {amount} accepted. Remaining balance: {student.balance}.")

    def check_student_balance(self, student_id): # Display the current balance for a student.
        if student_id not in self.students:
            raise ValueError(f"Student with ID {student_id} not found.")
        student = self.students[student_id]
        print(f"Student '{student.name}' has an outstanding balance of {student.balance}.")

    def show_courses(self): # Display all available courses.
        if not self.courses:
            print("No courses available.")
        else:
            print("Available courses:")
            for course in self.courses:
                print(f"ID: {course.course_id}, Name: {course.name}, Fee: {course.fee}")

    def show_registered_students(self): # Display all registered students
        if not self.students:
            print("No students registered.")
        else:
            print("Registered students:")
            for student_id, student in self.students.items():
                print(f"ID: {student_id}, Name: {student.name}, Email: {student.email}")

    def show_students_in_course(self, course_id): # Display all students enrolled in a specific course.
        course = next((course for course in self.courses if course.course_id == course_id), None)
        if not course:
            raise ValueError(f"Course with ID {course_id} not found.")
        enrolled_students = [
            student for student in self.students.values() if course in student.courses
        ]
        if not enrolled_students:
            print(f"No students enrolled in course '{course.name}'.")
        else:
            print(f"Students enrolled in course '{course.name}':")
            for student in enrolled_students:
                print(f"ID: {student.student_id}, Name: {student.name}")


# menu-driven interface for testing the system
def main():
    system = RegistrationSystem()
    while True:
        print("\nMenu:")
        print("1. Add Course")
        print("2. Register Student")
        print("3. Enroll Student in Course")
        print("4. Process Payment")
        print("5. Check Student Balance")
        print("6. Show All Courses")
        print("7. Show All Registered Students")
        print("8. Show Students in Course")
        print("9. Exit")
        choice = input("Enter your choice: ")
        try:
            if choice == "1":
                course_id = input("Enter course ID: ")
                name = input("Enter course name: ")
                fee = float(input("Enter course fee: "))
                system.add_course(course_id, name, fee)
            elif choice == "2":
                student_id = input("Enter student ID: ")
                name = input("Enter student name: ")
                email = input("Enter student email: ")
                system.register_student(student_id, name, email)
            elif choice == "3":
                student_id = input("Enter student ID: ")
                course_id = input("Enter course ID: ")
                system.enroll_in_course(student_id, course_id)
            elif choice == "4":
                student_id = input("Enter student ID: ")
                amount = float(input("Enter payment amount: "))
                system.calculate_payment(student_id, amount)
            elif choice == "5":
                student_id = input("Enter student ID: ")
                system.check_student_balance(student_id)
            elif choice == "6":
                system.show_courses()
            elif choice == "7":
                system.show_registered_students()
            elif choice == "8":
                course_id = input("Enter course ID: ")
                system.show_students_in_course(course_id)
            elif choice == "9":
                print("Exiting system. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
