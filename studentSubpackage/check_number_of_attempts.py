# OOP-model for a university: student submodule
import course as crs

def check_number_of_attempts(self, course_name):
	"""checks past exam_score-records for the given course and
	evaluates for the case of '3rd attempt with result >E<'
	or alternatively
	evaluates for the case of '2nd attempt with result >E<' """

	for key, value in self.exam_scores[course_name].items():

		# check for existing score-records
		if key == "grades":
			course_grades = value

			# scenario for a 3rd failed attempt
			if (len(course_grades) >= 3) and (course_grades[-1] == "E"):

				self.student_instances.pop(self.student_instances.index(self))
				self.study_status = "Dropped out"
				self.dropout_instances.append(self)
				print(f"{self.first_name} {self.last_name} failed '{course_name}' 3 times! \n"
					  f"current status: {self.exam_scores} \n"
					  f"Exmatriculation was proceeded \n")

				course_match = [course for course in crs.Course.search_instance_by_name(course_name)]
				# apply the following steps on all affected (examined) courses
				for course in course_match:

					course.participants.pop(course.participants.index(self))
					course.participants_count = len(course.participants)

					self.enrolled_courses.pop(self.enrolled_courses.index(course))
					self.enrolled_courses_count = len(self.enrolled_courses)

					return f"{self.first_name} {self.last_name} failed '{course_name}' 3 times. Exmatriculation was proceeded"

			# scenario for a 2nd failed attempt
			else:
				print(f"{self.first_name} {self.last_name} failed a 2nd attempt on '{course_name}'. \n"
					   f"current status: {self.exam_scores} \n")

		# In case there are no score-records so far
		else:
			return "no grade records so far!"

