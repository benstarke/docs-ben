from django.shortcuts import render
from django.contrib import messages
from testemails.settings import EMAIL_HOST_USER
from . import forms
from django.core.mail import send_mail

# Create your views here.
#DataFlair #Send Email
def subscribe(request):
    sub = forms.Subscribe()
    if request.method == 'POST':
        sub = forms.Subscribe(request.POST)
        subject = 'Welcome to BenstarDjango'
        msg = 'Hope you are enjoying your Django Tutorials'
        recepient = str(sub['Email'].value())
        send_mail(subject, 
            msg, EMAIL_HOST_USER, [recepient], fail_silently = False)
        messages.success(request,f'Email successful sent to {recepient}')
    return render(request, 'trytest/index.html', {'form':sub})