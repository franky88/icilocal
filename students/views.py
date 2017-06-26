from django.shortcuts import render, get_object_or_404, redirect
from .models import Student
from .forms import StudentForm
# Create your views here.
def studentList(request):
	student_list = Student.objects.all().order_by("-date_registered", "-date_updated")
	context = {
		"title": "student list",
		"studentlist": student_list,
	}
	return render(request, "students/student_list.html", context)

def studentDetail(request, pk):
	student_instance = get_object_or_404(Student, pk=pk)
	context = {
		"title": "student details",
		"instance": student_instance,
	}
	return render(request, "students/student_detail.html", context)

def studentAdd(request):
	form = StudentForm(request.POST or None)
	if request.method == "POST":
		if form.is_valid():
			instance=form.save(commit=False)
			instance.save()
			return redirect("student:detail", pk=instance.id)
	context = {
		"title": "student add",
		"form": form,
	}
	return render(request, "students/student_add.html", context)