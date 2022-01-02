import course
import person

from professorSubpackage.professor import Professor
from professorSubpackage.teach_course import teach_course
from professorSubpackage.drop_course import drop_course

from studentSubpackage.student import Student
from studentSubpackage.enroll_into_course import enroll_into_course
from studentSubpackage.write_exam import write_exam
from studentSubpackage.get_grade import get_grade
from studentSubpackage.check_number_of_attempts import check_number_of_attempts
from studentSubpackage.accomplish_course import accomplish_course
from studentSubpackage.check_progress import check_progress


print("\n")


c1 = course.Course("Py", 5, "Info")
print(c1)

p1 = Professor("van Rossum", "Guido", 65)
print(p1)

s1 = Student("Albert", "Josh", 27)
print(s1)
