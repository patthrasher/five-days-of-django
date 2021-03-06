from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm


def index(request) :
    context = {
    'title' : 'Allen Chase',
    'header' : 'Allen Chase Home Building',
    }
    return render(request, 'chasesite/index.html', context)
    # return HttpResponse('hola chase')


def contact_view(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "chasesite/email.html", {'form': form})


def success_view(request):
    return HttpResponse('Success! Thank you for your message.')
