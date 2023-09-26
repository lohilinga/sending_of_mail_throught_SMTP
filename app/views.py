from django.shortcuts import render
from django.http import HttpResponse
from app.forms import *
from django.core.mail import *

# Create your views here.


def registration(request):
    USFO=Userform()
    PFO=Profileform()
    d={'USFO':USFO,'PFO':PFO}

    if request.method=='POST' and request.FILES:

        UFDO=Userform(request.POST)
        PFDO=Profileform(request.POST,request.FILES)
        if UFDO.is_valid() and PFDO.is_valid():
            MUFDO=UFDO.save(commit=False)
            MUFDO.set_password(UFDO.cleaned_data['password'])
            MUFDO.save()
            
            MPFDO=PFDO.save(commit=False)
            MPFDO.username=MUFDO
            MPFDO.save()
            send_mail('registration',
                      'thanku for registration ',
                      'lohilinga258963@gmail.com',
                      [MUFDO.email],
                      fail_silently=False
                      )
            return HttpResponse('Successfully')
        return HttpResponse('Not done properly')
     

    return render(request,'registration.html',d)
