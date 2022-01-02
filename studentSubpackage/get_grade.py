# OOP-model for a university: student submodule

# Random-module for generating a random integer in between a certain interval
from random import randint

def get_grade(self):
	"""generates a random exam score and assigns it to a grade"""

	grade = randint(40, 62)

	if grade < 60:
		return "E"

	elif grade >= 90:
		return "A"

	elif grade >= 80:
		return "B"

	elif grade >= 70:
		return "C"

	elif grade >= 60:
		return "D"

	else:
		print("wrong score")
