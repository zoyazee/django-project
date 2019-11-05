from django.test import TestCase
from student.models import Student
from teacher.models import Teacher
import datetime 

class StudentCourseTestCase(TestCase):
	def setUp(self):
		self.student_a = Student.objects.create(
			id="34678922",
			first_name = "Alisha",
			last_name = "Wanjiku",
			date_of_birth = datetime.date(2001,6,9),
			gender = "female",
			registration_number = "9200",
			email = "ali@gmail.com",
			phone_number = "0710989010",
			date_joined = datetime.date.today(),
			)
		self.student_b = Student.objects.create(
			first_name = "Beatrice",
			last_name = "Wanja",
			date_of_birth = datetime.date(2004,4,7),
			gender = "female",
			registration_number = "9001",
			email = "Wanja@gmail.com",
			phone_number = "0720844673",
			date_joined = datetime.date.today(),
			)
		self.teacher_a = Teacher.objects.create(
			first_name = "John",
			last_name = "Owour",
			gender = "male",
			email = "john@mobiledevelopment.com",
			phone_number ="0724675887",
			profession = "mobiledevelopment",
			date_employed = datetime.date.today(),
			id_number = 30965784,
			
	        )
		self.teacher_b = Teacher.objects.create(
			first_name = "David",
			last_name = "Mwai",
			gender = "male",
			email = "mwai@akirachix.com",
			phone_number ="0724675800",
			profession = "python",
			date_employed = datetime.date.today(),
			id_number = 30165784,
			)
		self.teacher_c = Teacher.objects.create(
			first_name = "Immanuel",
			last_name = "Wanjohi",
			gender = "male",
			email = "emmanuel@akirachix.com",
			phone_number ="0724000087",
			profession = "Electronics",
			date_employed = datetime.date.today(),
			id_number = 32965784,
			
			)

	def test_student_can_join_a_teacher(self):
		self.student_a.teachers.add(self.teacher_a)
		self.assertEqual(self.student_a.teachers.count(),1)
		self.student_a.teachers.add(self.teacher_b)
		self.assertEqual(self.student_a.teachers.count(),2)
		self.student_a.teachers.add(self.teacher_c)
		self.assertEqual(self.student_a.teachers.count(),3)

	# def test_student_can_join_many_courses(self):
	# 	self.student_b.courses.add(self.python,self.javascript,self.design)
	# 	self.assertEqual(self.student_b.courses.count(),3)
		   	