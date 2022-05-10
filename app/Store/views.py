from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import eBook


def cat_room(request):
    cats = {'cats': eBook.objects.all()}
    # text = 'any'
    return render(request, "Store\index.html", cats)
    # return HttpResponse(request, text)