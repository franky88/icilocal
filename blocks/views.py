from django.shortcuts import render, get_object_or_404
from .models import Block
# Create your views here.
def blockList(request):
	block_list=Block.objects.all()
	context={
		"title": "block list",
		"blocklist": block_list,
	}
	return render(request, "blocks/block_list.html", context)

def blockDetail(request, pk):
	instance=get_object_or_404(Block, pk=pk)
	context = {
		"title": "block details",
		"instance": instance,
	}
	return render(request, "blocks/block_detail.html", context)