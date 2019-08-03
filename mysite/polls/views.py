from django.shortcuts import render
# to call view you need to map it to a URL in the polls folder

# Create your views here.
from django.http import HttpResponse
# from django.template import loader


# wire views into polls/urls and those into mysite/urls.py
def index(request):
	return render(request, 'polls/index.html')
	# template = loader.get_template('polls/index.html')
	# return HttpResponse(template.render())
    # return HttpResponse("Hello, world. You're at the polls index. In Tobis app it sais: NPC Calculator")