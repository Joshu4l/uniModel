# OOP-model for a university: student module

# Import the other class modules
import course as crs
import person as prs

# Definition of the <Student> class
class Student(prs.Person):

    student_count = int(0)
    student_instances = []
    dropout_instances = []
    ects_tbd = 180

    def __init__(self, last_name, first_name, age):  # Initialize a Student
        super().__init__(last_name, first_name, age)  # <-- ...inherit these initialization-parameters from the super class

        Student.student_count += 1
        Student.student_instances.append(self)

        # Beside the inherited attributes, introduce the following ones to <self> (= to the initialized instance)
        self.enrollment_number = f"S-{Student.student_count:04d}"
        self.study_status = "Active"

        self.enrolled_courses = []
        self.enrolled_courses_count = 0

        self.accomplished_courses = []
        self.accomplished_courses_count = 0

        self.ects_count = 0
        self.exam_scores = {}
        print(f"Student object '{self.first_name} {self.last_name}', age: {self.age}, enrollment number: {self.enrollment_number} was created. \n")

    # IMPORTED STUDENT-METHODS FROM THE <studentSubpackage>
    from studentSubpackage.check_progress import check_progress
    from studentSubpackage.enroll_into_course import enroll_into_course
    from studentSubpackage.write_exam import write_exam
    from studentSubpackage.get_grade import get_grade
    from studentSubpackage.check_number_of_attempts import check_number_of_attempts
    from studentSubpackage.accomplish_course import accomplish_course
