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