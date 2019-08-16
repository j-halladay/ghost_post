from django.shortcuts import render
from ghost_post.models import Message
from ghost_post.forms import AddMessage
from django.http import HttpResponseRedirect
from django.urls import reverse


def homepage(request, *args, **kwargs):
    html = 'homepage.html'

    items = Message.objects.all().order_by('-created')
    return render(request, html, {"messages": items})


def boasts(request, *args, **kwargs):
    html = 'homepage.html'
    items = Message.objects.all().filter(is_boast=True).order_by('-created')
    return render(request, html, {"messages": items})


def roasts(request, *args, **kwargs):
    html = 'homepage.html'
    items = Message.objects.all().filter(is_boast=False).order_by('-created')
    return render(request, html, {"messages": items})


def likes(request, *args, **kwargs):
    html = 'homepage.html'
    items = Message.objects.all().order_by('-like')
    return render(request, html, {"messages": items})


def like(request, id, *args, **kwargs):
    html = 'homepage.html'
    item = Message.objects.get(id=id)
    item.like = item.like + 1
    item.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def unlike(request, id, *args, **kwargs):
    html = 'homepage.html'
    item = Message.objects.get(id=id)
    item.like = item.like - 1
    item.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def addmessage(request, *args, **kwargs):
    html = 'genericform.html'
    if request.method == "POST":
        form = AddMessage(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            m = Message.objects.create(
                text=data['text'], is_boast=data['is_boast'], like=0)
            return HttpResponseRedirect(reverse('homepage'))
    form = AddMessage()

    return render(request, html, {'form': form})
