from django.shortcuts import render, HttpResponse

from . import models
# Create your views here.


def home(request):
    return render(request, 'post/index.html', context={"posts": models.Post.objects.all()})
