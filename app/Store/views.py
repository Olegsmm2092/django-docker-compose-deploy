from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import eBook


def cat_room(request):
    cats = {'cats': eBook.objects.all()}
    return render(request, "Store\index2.html", cats)