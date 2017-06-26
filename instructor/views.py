from django.shortcuts import render, get_object_or_404
from .models import Instructor
# Create your views here.
def instructorList(request):
	instructor_list=Instructor.objects.all()
	context={
		"title": "instructor list",
		"instructorlist": instructor_list,
	}
	return render(request, "instructor/instructor_list.html", context)

def instructorDetail(request, pk):
	instructor_instance=get_object_or_404(Instructor, pk=pk)
	context={
		"title":"instructor details",
		"instance": instructor_instance,
	}
	return render(request, "instructor/instructor_detail.html", context)