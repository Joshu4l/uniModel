# OOP-model for a university: professor module
import course as crs

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
