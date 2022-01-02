# OOP-model for a university: student submodule
import course as crs

def enroll_into_course(self, course_name):
	"""Let the student pick up a course"""
	# check for the sheer existence of the given course
	if course_name.lower() in crs.Course.course_list:

		# pick out every matching course instance <i>
		for i in crs.Course.search_instance_by_name(course_name.lower()):

			# also check if student is already enrolled!
			if not self in i.participants:

				# Add the <Student> instance to the course's list of participants
				i.participants.append(self)
				i.participants_count = len(i.participants)
				# Add the given <Course> instance to the student's personal list of enrolled courses
				self.enrolled_courses.append(i)
				self.enrolled_courses_count = len(self.enrolled_courses)
				# Show an enrollment feedback
				return f"{self.first_name} {self.last_name} was enrolled in course '{course_name}'. \n"

			# in case the student is already among the course's participants
			else:
				return f"{self.first_name} {self.last_name} is already enrolled in '{course_name}'! \n"

	# if no identically-named course exists
	else:
		return f"No such course '{course_name}' available to enroll in! \n"
