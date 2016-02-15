from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from .models import ImgMessage
from .forms import ImgMessageForm


def index(request):
	all_img = ImgMessage.objects.all()
	context = { 'all_img': all_img } 
	return render(request, 'img/index.html', context)

def new(request):
	if request.method == 'POST':
		form = ImgMessageForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(reverse('index'))
		#else:
		#	return render(request, 'new.html', 
		#		{'error_message': "Error",})

	else:
		form = ImgMessageForm()
		return render(request, 'img/new.html', {'form': form})

def add(request):
	t= { request.POST['photo'], request.POST['comment'] }
	context = { 'all_img': t } 
	imgmes= ImgMessage(img = request.POST['photo'],
					   text= request.POST['comment'])
	imgmes.save()
	return render(request, 'img/new.html', context)