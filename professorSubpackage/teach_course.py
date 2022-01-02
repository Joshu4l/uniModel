# OOP-model for a university: professor module
import course as crs

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
		# Make the professor responsible for that course
		course.professor = self

	# Check if the course is among the professor's personal course list
	if not course_name.lower() in self.supervised_courses:
		# add the course name to the professor's personal course list
		self.supervised_courses.append(course_name.lower())
		print(f"Professor {self.last_name} began to teach course '{course_name}'. \n"
			  f"His courses now are: {self.supervised_courses} \n")
	else:
		print(f"Professor {self.last_name} is already teaching '{course_name}'!")