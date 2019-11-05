from django.test import TestCase
from teacher.models import Teacher
from course.models import Course
import datetime 

class TeacherCourseTestCase(TestCase):
	def setUp(self):
		self.teacher_a = Teacher.objects.create(
			first_name = "Tina",
	        last_name = "Nanzala",
	        gender = "female",
	        email = "nanazalatina@gmail.com",
	        phone_number = "0743234567",
	        profession = "Graphic designer",
	        date_employed =datetime.date.today(),
	        id_number = 35674489,
			)
		self.teacher_b = Teacher.objects.create(
			first_name = "Sharon",
	        last_name = "Akoth",
	        gender = "female",
	        email = "akoth@gmail.com",
	        phone_number = "0743234765",
	        profession = "Graphic designer",
	        date_employed =datetime.date.today(),
	        id_number = 35674984,
			)
		self.graphic = Course.objects.create(
			name="Graphic",
	        duration_in_months=9,
	        start_date=datetime.date.today(),
	        end_date=datetime.date.today(),
	        description="fronteddeveloper",
	        )
		self.javascript = Course.objects.create(
			name="JavaScript",
	        duration_in_months=7,
	        start_date=datetime.date.today(),
	        end_date=datetime.date.today(),
	        description="fronteddeveloper",
	        )
		self.design = Course.objects.create(
			name="Design",
	        duration_in_months=5,
	        start_date=datetime.date.today(),
	        end_date=datetime.date.today(),
	        description="fronteddeveloper",
	        )

	def test_course_can_be_trained_by_a_teacher(self):
		self.python.teacher = self.teacher_a
		self.assertEqual(self.python.teacher, self.teacher_a)
		

    def test_many_courses_can_be_trained_by_one_trainer(self):
    	self.python.teacher = self.teacher_b
        self.java.teacher = self.teacher_b
        self.assertEqual(self.java.teacher,self.python.teacher)