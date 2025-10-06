from django.shortcuts import render

from event.models import Event_speaker, About, Sponsor, Authors, Partner, Link


def index(request):
    speaker=Event_speaker.objects.all()
    about=About.objects.all()[:1]
    sponsor=Sponsor.objects.all()
    partner=Partner.objects.all().order_by("-id")
    link=Link.objects.all()
    return render(request, 'index.html',{"speaker":speaker,"about":about,"sponsor":sponsor,'partner':partner, 'link':link} )


def registration(request):
    link=Link.objects.all()

    return render(request, 'registration.html', {'link':link})

def venue(request):
    return render(request, 'venue.html')

def authors(request):
    author=Authors.objects.all()[:1]
    return render(request, 'authors.html',{"author":author} )



def about(request):
    about=About.objects.all()[:1]

    return render(request, 'about.html',{'about':about})

def schedule(request):
    # committe=Committee.objects.all()[:1]
    speaker=Event_speaker.objects.all()

    return render(request, 'schedule.html', {"speaker":speaker})
