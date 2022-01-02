# OOP-model for a university: student module
import person as prs
import course as crs

class Professor(prs.Person):

    staff_count = 0
    staff_instances = []

    def __init__(self, last_name, first_name, age):  # Initialize a Professor, and ...
        super().__init__(last_name, first_name, age)  # <-- ...inherit these initialization-parameters from the super class
        Professor.staff_instances.append(self)

        Professor.staff_count += 1  # Beside the inherited attributes, ...
        self.staff_number = f"T-{Professor.staff_count:04d}" # ... introduce a staff number to <self>
        self.supervised_courses = []  # ... introduce a personal course list to <self>
        print(f"Professor object '{self.first_name} {self.last_name}', age: {self.age}, enrollment number: {self.staff_number} was created. \n")

    def teach_course(self, course_name, course_ects, course_domain):
        """causes the following actions to be executed:
        Check if a <Course> instance with such a <course_name> already exists and if not, instantiate one.
        Make the professor start teaching a course by adding that course to his personal list.
        Make the professor appear as the <Course>'s <.professor> attribute-value."""

        # Check if the course is among the instances of <Course> yet
        if not course_name.lower() in crs.Course.course_list:
            # Instantiate a new course with the <course_name>, the professor started teaching
            crs.Course(course_name, course_ects, course_domain)

        # if there is a match for the <course_name> input
        for course in crs.Course.search_instance_by_name(course_name):
            # Add the student to the course's participants list
            course.professor = self

        # Check if the course is among the professor's personal course list
        if not course_name.lower() in self.supervised_courses:
            # add the course name to the professor's personal course list
            self.supervised_courses.append(course_name.lower())
            print(f"Professor {self.last_name} began to teach course '{course_name}'. \n"
                  f"His courses now are: {self.supervised_courses} \n")
        else:
            print(f"Professor {self.last_name} is already teaching '{course_name}'!")


    def drop_course(self, course_name):
        """causes a professor to stop teaching a course"""

        # Search for matching courses and ...
        for course in crs.Course.search_instance_by_name(course_name.lower()):
            # ... reset the <Course>'s professor attribute
            if course.professor == self:
                course.professor = None

        # Search for matching courses in the professor's individual supervised courses and ...
        if course_name.lower() in self.supervised_courses:
            c = self.supervised_courses.index(course_name.lower())
            # ... delete the respective course from in there
            self.supervised_courses.pop(c)
            print(f"Professor {self.last_name} stopped teaching '{course_name}'. \n"
                  f"His courses now are: {self.supervised_courses}. \n")

        # In case of no search results, say so
        else:
            print(f"No such course '{course_name}' supervised by Professor {self.last_name}.")
