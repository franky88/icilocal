from django.shortcuts import render
from .models import SchoolForm
# Create your views here.
def schoolFormList(request):
	schoolform_list=SchoolForm.objects.all()
	context={
		"title": "school form list",
		"schoolformlist": schoolform_list,
	}
	return render(request, "schoolforms/schoolform_list.html", context)