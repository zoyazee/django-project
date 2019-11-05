from django.test import TestCase
from .models import Student
from student.forms import StudentForm
from django.test import Client
from django.urls import reverse
import datetime


class StudentTestCase(TestCase):
	def setUp(self):
		self.student = Student(
			first_name = "Joy",
			last_name = "Wanja",
			date_of_birth = datetime.date(2000,4,9),
			gender = "female",
			registration_number = "1234",
			email = "joygathigira@gmail.com",
			phone_number = "0710950673",
			date_joined = datetime.date.today(),
			)

	def test_full_name_contains_first_name(self):
		self.assertIn(self.student.first_name, self.student.full_name())

	def test_full_name_contains_last_name(self):
		self.assertIn(self.student.last_name, self.student.full_name())

	def test_age_is_always_above_17(self):
		self.assertFalse(self.student.clean() < 17 )

	def test_age_is_always_below_30(self):
		self.assertFalse(self.student.clean() > 30 )

class AddStudentTestCase(TestCase):
	def setUp(self):
		self.data = {
		"first_name": "Joy",
		"last_name": "Gathigira",
		"date_of_birth": datetime.date(1996,9,4,),
		"gender": "Female",
		"registration_number": "3456",
		"email": "zoya@gmail.com",
		"phone_number": "0752705031",
		"date_joined": datetime.date.today(),
		
		}
		self.bad_data ={
		"first_name": "Joy",
		"last_name": "Gathigira",
		"date_of_birth": datetime.date(1996,9,4),
		"gender": "Female",
		"registration_number": "3456",
		"email": "zoygmaicom",
		"phone_number": "0752705031",
		"date_joined": datetime.date.today(),

		}

	def test_student_form_accepts_valid_data(self):
		form = StudentForm(self.data)
		self.assertTrue(form.is_valid())

	def test_student_form_rejects_invalid_data(self):
		form = StudentForm(self.bad_data)
		self.assertFalse(form.is_valid())

	def test_add_student_view(self):
	    client = Client()
	    url = reverse("add_student")
	    response = client.post(url,self.data)
	    self.assertEqual(response.status_code,200)

	def test_add_student_view_bad_data(self):
	    client = Client()
	    url = reverse("add_student")
	    response = client.post(url,self.bad_data)
	    self.assertEqual(response.status_code,400)    	




# Create your tests here.
