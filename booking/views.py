from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import ContactForm


def homepage(request):
    return render(request, 'index.html')


def services(request):
    return render(request, 'services.html')


def contact(request):
    submitted = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            assert false
            return HttpResponseRedirect('/contact?submitted=True')

    else:
        form = ContactForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'contact.html', {'form': form, 'submitted': submitted})
