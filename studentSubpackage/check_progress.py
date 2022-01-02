# OOP-model for a university: student submodule

def check_progress(self):
	"""check a student's progress in terms of ects"""

	if self.ects_count >= self.ects_tbd:
		return f"Congrats to {self.first_name} {self.last_name}: Graduation achieved! :)"

	else:
		return f"{self.first_name} {self.last_name}'s ECTS-count: {self.ects_count}/{self.ects_tbd} \n"
