# OOP-model for a university: course module

class Course:

    instances = []
    course_list = []
    course_number = 0000

    def __init__(self, course_name, course_ects, course_domain):

        Course.instances.append(self)
        self.course_name = course_name.lower()

        # Check if the course already exists, otherwise add its <course_name> to the list of offered courses
        if not course_name.lower() in Course.course_list:
            Course.course_list.append(self.course_name)

        self.course_ects = course_ects
        self.course_domain = course_domain
        self.professor = None
        self.participants = []
        self.participants_count = 0

    def __str__(self):
        return f"Course name: {self.course_name}, ECTS: {self.course_ects}, Domain: {self.course_domain}"

    @classmethod
    def search_instance_by_name(cls, search_key):
        """list comprehension for getting all instances by a search key
        Works for all classes inheriting from <Person> !"""
        return [obj for obj in cls.instances if obj.course_name.lower() == search_key.lower()]
