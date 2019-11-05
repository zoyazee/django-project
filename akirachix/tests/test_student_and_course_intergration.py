from django.test import TestCase
from student.models import Student
from course.models import Course
import datetime 

class StudentCourseTestCase(TestCase):
	def setUp(self):
		self.student_a = Student.objects.create(
			id="34678900",
			first_name = "Anne",
			last_name = "Wanjiku",
			date_of_birth = datetime.date(2000,6,9),
			gender = "female",
			registration_number = "9283",
			email = "shiku@gmail.com",
			phone_number = "0710989000",
			date_joined = datetime.date.today(),
			)
		self.student_b = Student.objects.create(
			first_name = "Beatrice",
			last_name = "Wangui",
			date_of_birth = datetime.date(2000,4,7),
			gender = "female",
			registration_number = "0001",
			email = "beatrice@gmail.com",
			phone_number = "0720830673",
			date_joined = datetime.date.today(),
			)
		self.python = Course.objects.create(
			name="Python",
	        duration_in_months=9,
	        start_date=datetime.date.today(),
	        end_date=datetime.date.today(),
	        description="backeneddeveloper",
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

	def test_student_can_join_a_course(self):
		self.student_a.courses.add(self.python)
		self.assertEqual(self.student_a.courses.count(),1)
		self.student_a.courses.add(self.javascript)
		self.assertEqual(self.student_a.courses.count(),2)
		self.student_a.courses.add(self.design)
		self.assertEqual(self.student_a.courses.count(),3)

	def test_student_can_join_many_courses(self):
		self.student_b.courses.add(self.python,self.javascript,self.design)
		self.assertEqual(self.student_b.courses.count(),3)
		   	