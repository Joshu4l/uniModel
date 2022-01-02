# OOP-model for a university: student submodule

def accomplish_course(self, course_name):
	"""shifts a course from the student's enrolled list into his/her accomplished list"""

	# Check if the given course even is among the student's enrolled ones
	for i in self.enrolled_courses:

		# if so, pick the matching course object, and...
		if course_name.lower() == i.course_name:

			# ... delete the student from its participants
			i.participants.pop(i.participants.index(self))
			i.participants_count = len(i.participants)

			# ...delete it from the student's enrolled ones
			self.enrolled_courses.pop(self.enrolled_courses.index(i))
			self.enrolled_courses_count = len(self.enrolled_courses)

			# ...add it to the student's accomplished ones
			self.accomplished_courses.append(i)
			self.accomplished_courses_count = len(self.accomplished_courses)
			self.ects_count += i.course_ects

		# if there is no such course name among the student's enrolled ones
		else:
			print(f"No such course '{course_name}', in which {self.first_name} {self.last_name} is enrolled in currently")
