from django.shortcuts import render
from .forms import TeacherForm
from .models import Teacher
from django.shortcuts import redirect
from django.http import HttpResponse

def add_teacher(request):
	if request.method == "POST":
		form = TeacherForm(request.POST)
		if form.is_valid():
			form.save()
			# return redirect("list_teachers")
		else:
			return HttpResponse("invalid data", status =400)

	else:
		form = TeacherForm()

	return render(request,"add_teacher.html",{"form":form})

def list_teachers(request):
	teachers = Teacher.objects.all()
	return render(request,"all_teachers.html",{"teachers":teachers})

def teacher_details(request,pk):
	teacher = Teacher.objects.get(pk=pk)
	return render(request,"teacher_details.html",{"teacher":teacher})

def edit_teacher(request,pk):
	teacher = Teacher.objects.get(pk=pk)
	if request.method=="POST":
		form = teacherForm(request.POST,instance=teacher)
		if form.is_valid:
			form.save()
			return redirect("list_teachers")
	else:
		form=teacherForm(instance=teacher)

	return render(request,"edit_teacher.html",{"form":form})



	# form = TeacherForm()
	
# Create your views here.
