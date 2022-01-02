# OOP-model for a university: student module -> student subpackage
import course as crs

def write_exam(self, course_name):

	# Get a random score and assign it to a grade
	grade = self.get_grade()
	# Generate a result list for all courses that are named like the search-key
	course_match = [course for course in crs.Course.search_instance_by_name(course_name)]

	# Check if there even is an existing course for that exam attempt
	if not course_match:
		print(f"no such course '{course_name} existing'")
	# In case there was found an existing course instance for examination
	else:

		# apply the following steps on every matching course that was found
		for course in course_match:

			# Check if the student even is enrolled in that course
			if self in course.participants:


				# Check IF there are already ANY EXISTING GRADES for that <Student> instance with that <course_name>
				if course_name.lower() in self.exam_scores.keys():

					# Catch the CURRENT GRADES-RECORD for that <Student> instance and for that <course_name>
					grades_record = self.exam_scores[course_name.lower()]["grades"]

					# if the LATEST ATTEMPT was already PASSED (which means, not an 'E')
					if grades_record[-1] != "E":
						print(f"{self.first_name} {self.last_name} already passed '{course_name}' successfully!")
						print(f"current status: {self.exam_scores} \n")

					# if the LATEST ATTEMPTS were FAILED in the past but the CURRENT ATTEMPT IS SUCCESSFUL
					elif (grades_record[-1] == "E") and (grade != "E"):
						self.exam_scores[course_name.lower()]["grades"].append(grade)
						self.exam_scores[course_name.lower()]["trials"] += 1
						print(f"{self.first_name} {self.last_name}'s latest attempt on '{course_name}' was successful: grade >{grade}<")
						print(f"current status: {self.exam_scores} \n")
						self.accomplish_course(course_name.lower())

					# if the LATEST ATTEMPTS were FAILED in the past and the CURRENT ATTEMPT IS FAILED AGAIN
					else:  # (grades_record[-1] == "E") and (grade == "E"):
						self.exam_scores[course_name.lower()]["grades"].append(grade)
						self.exam_scores[course_name.lower()]["trials"] += 1
						# Also check if the number of attempts still lies within the range of the course's max. strikes
						self.check_number_of_attempts(course_name.lower())


				# Case 'has not written any exams yet'
				else:

					# if this is the FIRST AND SUCCESSFUL ATTEMPT for that course
					if grade != "E":
						self.exam_scores[course_name.lower()] = {"grades": [grade], "trials": 1}  # create an <.exam_scores> entry for a pass
						print(f"{self.first_name} {self.last_name} passed '{course_name}' at the fist attempt with result >{grade}<.")
						print(f"current status: {self.exam_scores} \n")
						self.accomplish_course(course_name.lower())

					# if this is the FIRST ATTEMPT for that course which is FAILED
					else:
						self.exam_scores[course_name.lower()] = {"grades": [grade], "trials": 1}  # or create an <.exam_scores> entry for a failure
						print(f"{self.first_name} {self.last_name} made a 1st attempt on '{course_name}' and failed.")
						print(f"current status: {self.exam_scores} \n")


			# In case the student isn't even enrolled in the respective course
			else:
				print(f"no examination possible! \n"
					  f"{self.last_name} {self.first_name} could not be found among the participants of '{course_name}'.")
