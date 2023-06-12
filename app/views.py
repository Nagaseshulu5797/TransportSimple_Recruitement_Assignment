from django.shortcuts import render
from app.models import *
# Create your views here.
from app.forms import *
from django.core.mail import send_mail
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView,ListView


def home(request):
    if request.session.get('username'):
        username=request.session.get('username')
        d={'username':username}
        return render(request, 'home.html',d)
    return render(request, 'home.html')

def register(request):
    UFO=UserForm()
    d={'UFO':UFO}
    if request.method=='POST':
        UFD=UserForm(request.POST)
        if UFD.is_valid():
            NSUD=UFD.save(commit=False)
            NSUD.set_password(UFD.cleaned_data['password'])
            NSUD.save()

            send_mail('Nagaseshulu', 'Registration success', 
            'seshulustra1234@gmail.com', [NSUD.email],
            fail_silently=False)
            return HttpResponseRedirect(reverse('user_login'))
        return HttpResponse('Data is not valid')
    return render(request, 'rigister.html',d)


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('un')  # Use get() to avoid KeyError if the field is missing
        password = request.POST.get('pw')
        user = authenticate(request, username=username, password=password)  # Pass the request object as the first argument

        if user is not None:
            login(request, user)
            request.session['username'] = username
            return HttpResponseRedirect(reverse('home'))
        else:
            return HttpResponse('Username or password is incorrect.')
    else:
        return render(request, 'user_login.html')


@login_required()
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

def quetion_details(request):
    QQ=Quetions.objects.all()
    d={'QQ':QQ}
    return render(request, 'quetion_details.html',d)

@login_required()
def quetion_form(request):
    QFO=QuetionsForm()
    d={'QFO':QFO}
    if request.method=='POST':
        QFD=QuetionsForm(request.POST)
        if QFD.is_valid():
            NSQD=QFD.save(commit=False)
            username=request.session.get('username')
            UO=User.objects.get(username=username)
            NSQD.user=UO
            NSQD.save()
            return HttpResponseRedirect(reverse('quetion_details'))
        return HttpResponse('Data is not valid')
    return render(request, 'quetion_form.html',d)


@login_required()
def answer_form(request):
    QFD=AnswersForm()
    d={'QFD':QFD}
    if request.method=='POST':
        AFD=AnswersForm(request.POST)
        if AFD.is_valid():
            NSAD=AFD.save(commit=False)
            username=request.session.get('username')
            UO=User.objects.get(username=username)
            NSAD.user=UO
            NSAD.save()
            return HttpResponseRedirect(reverse('quetion_details'))
        return HttpResponse('Data is not Valid')
    return render(request, 'answer_form.html',d)

class detailinfo(DetailView):
    template_name='detail_info.html'
    model=Quetions
    context_object_name='AO'
    

