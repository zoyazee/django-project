from django.test import TestCase
from .models import Course
from course.forms import CourseForm
from django.test import Client
from django.urls import reverse
import datetime


class AddCourseTestCase(TestCase):
	def setUp(self):
		self.data = {
		"name":"Software development",
	    "duration_in_months":5,
	    "start_date":datetime.date.today(),
	    "end_date":datetime.date.today(),
	    "description":"webdeveloper",
		
		}
		self.bad_data = {
		"name":"Software development",
	    "duration_in_months":"12yrs",
	    "start_date":datetime.date.today(),
	    "end_date":datetime.date.today(),
	    "description":"webdeveloper",
	    "teacher":"Valentine"

		}

	def test_course_form_accepts_valid_data(self):
		form = CourseForm(self.data)
		self.assertTrue(form.is_valid())

	def test_course_form_rejects_invalid_data(self):
		form = CourseForm(self.bad_data)
		self.assertFalse(form.is_valid())

	def test_add_course_view(self):
	    client = Client()
	    url = reverse("add_course")
	    response = client.post(url,self.data)
	    self.assertEqual(response.status_code,200)

	def test_add_course_view_bad_data(self):
	    client = Client()
	    url = reverse("add_course")
	    response = client.post(url,self.bad_data)
	    self.assertEqual(response.status_code,400)  

# Create your tests here.
