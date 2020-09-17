from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from .models import Names
from .forms import NameForm


def index(request) :
    all_items = Names.objects.all
    context = {
        'all_items' : all_items,
        'header' : 'Enter your name for some reason',
    }

    if request.method == 'POST' :
        form = NameForm(request.POST or None)

        if form.is_valid() :
            form.save()
            messages.success(request, ('Your Name Has Been Added To The Database!'))
            return render(request, 'names/index.html', context)

    else :
        return render(request, 'names/index.html', context)
