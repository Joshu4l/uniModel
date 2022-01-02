# OOP-model for a university: student module

import course as crs
import person as prs


class Professor(prs.Person):

    staff_count = 0
    staff_instances = []

    def __init__(self, last_name, first_name, age):  # Initialize a Professor, and ...
        super().__init__(last_name, first_name, age)  # <-- ...inherit these initialization-parameters from the super class
        Professor.staff_instances.append(self)

        Professor.staff_count += 1  # Beside the inherited attributes, ...
        self.staff_number = f"T-{Professor.staff_count:04d}" # ... introduce a staff number to <self>
        self.supervised_courses = []  # ... introduce a personal course list to <self>
        print(f"Professor object '{self.first_name} {self.last_name}', age: {self.age}, staff number: {self.staff_number} was created. \n")


    # IMPORTED STUDENT-METHODS FROM THE <studentSubpackage>
    from professorSubpackage.teach_course import teach_course
    from professorSubpackage.drop_course import drop_course


