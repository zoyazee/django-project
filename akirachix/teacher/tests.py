from django.test import TestCase
from .models import Teacher
from teacher.forms import TeacherForm
from django.test import Client
from django.urls import reverse
import datetime


class AddTeacherTestCase(TestCase):
	def setUp(self):
		self.data = {
		"first_name": "Valentine",
		"last_name": "Wangeci",
		"gender": "Female",
		"email": "vale@gmail.com",
		"phone_number": "0752705000",
	    "profession":"Python",
	    "id_number":"29345569",
		"date_employed": datetime.date.today(),
		
		}
		self.bad_data = {
		"first_name": "Valentine",
		"last_name": "Wangeci",
		"gender": "Female",
		"email": "valegmail.com",
		"phone_number": "0752705000",
	    "profession":"Python",
	    "id_number":"29345569",
		"date_employed": datetime.date.today(),

		}

	def test_teacher_form_accepts_valid_data(self):
		form = TeacherForm(self.data)
		self.assertTrue(form.is_valid())

	def test_teacher_form_rejects_invalid_data(self):
		form = TeacherForm(self.bad_data)
		self.assertFalse(form.is_valid())

	def test_add_teacher_view(self):
	    client = Client()
	    url = reverse("add_teacher")
	    response = client.post(url,self.data)
	    self.assertEqual(response.status_code,200)

	def test_add_teacher_view_bad_data(self):
	    client = Client()
	    url = reverse("add_teacher")
	    response = client.post(url,self.bad_data)
	    self.assertEqual(response.status_code,400) 

# Create your tests here.
