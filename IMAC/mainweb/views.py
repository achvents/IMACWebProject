from django.shortcuts import render

from .models import IMACevents, article, member

def home(request):
    num_member = member.objects.all().count()
    num_events = IMACevents.objects.all().count()
    num_article = article.objects.all().count()

    context = {
        'num_member' : num_member,
        'num_events' : num_events,
        'num_article' : num_article,
    }

    return render(request, 'home.html', context=context)

def error(request):
    return render(request, 'error.html')

def home(request):
	return render(request,'home.html')

def login(request):
	return render(request,'login.html')

from django.template import RequestContext


def handler404(request, *args, **argv):
    context = RequestContext(request)
    response = render(None, 'error.html', context=context)
                                  
    response.status_code = 404
    return response


def handler500(request, *args, **argv):
    response = render('error.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response #Gatau bisa ato ngga

def handle_not_found(request, exception):
    return render(request, "error.html")