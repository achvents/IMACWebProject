from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib import messages
from .forms import LoginForm, RegistrationForm
from .models import IMACevents, article, User, Nama_Manajer, Divisi
from django.http import HttpResponseRedirect,JsonResponse
from datetime import datetime
from django.views import View
import io,csv
from django.template import RequestContext

#Page Login
def user_login(request):
    form = LoginForm(request.POST or None)
    if request.POST:
        if form.is_valid():
            user = form.login(request)
            if user:
                login(request, user)
                return redirect('yourmanajer')# Redirect to a success page.
        else:
            messages.error(request,'Email or Password do not match')
            form = LoginForm()
    else:
        form = LoginForm()
    context = {'form': form,}

    return render(request, 'registration/login.html', context)

#Page Registration (Belum ada templatenya)
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(data = request.POST)
        if form.is_valid():
            user = form.save()
            email = user.email
            password = user.password
            u = authenticate(email = email, password = password)
            login(request,u)
            return redirect('home')
    else:
        form = RegistrationForm()

    return render(request,'registration/register.html',{'form':form,})

#Homepage (Tapi belum dipake, nanti bisa dipake buat nampilin event terbaru)
"""
def home(request):
    num_member = User.objects.all().count()
    num_events = IMACevents.objects.all().count()
    num_article = article.objects.all().count()

    context = {
        'num_member' : num_member,
        'num_events' : num_events,
        'num_article' : num_article,
    }

    return render(request, 'home.html', context=context)
"""

#Page error dedicated
def error(request):
    return render(request, 'error.html')

#Page home sekarang(Static)
def home(request):
	return render(request,'home.html')

#Page pengumuman/admitted, nanti diganti page user profile 
@login_required
def admitted(request):
    current_user = request.user
    if current_user.usergroup == 'x':
        nama = current_user.name
        jurusan = current_user.jurusan
        nrp = current_user.nrp
        id_imac = current_user.IMACid
        context = {
                    'nama' : nama,
                    'jurusan' : jurusan,
                    'nrp' : nrp,
                    'id_imac' : id_imac,
                }
        return render(request,'admitted.html', context=context)
    else:
        pass
    return render(request,'rejected.html')

#Page handler error 404 sama 500
def handler404(request, *args, **argv):
    context = RequestContext(request)
    response = render(None, 'error.html', context=context)
                                  
    response.status_code = 404
    return response


def handler500(request, *args, **argv):
    response = render('error.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response #Gatau bisa ato ngga

def handle_not_found(request, exception):
    return render(request, "error.html")

#Page buat nyari query manajer, jadiin view ini buat contoh narik data dari db 
def your_manajer(request):
    my_manager = Nama_Manajer.objects.filter(user=request.user)[0]
    my_divisi = Divisi.objects.filter(user=request.user)
    nama_manager =my_manager.manajer
    nama_divisi = my_divisi
    context = {
        'nama_manager': nama_manager,
        'nama_divisi': nama_divisi,
    }
    return render(request,'nama_manajer.html', context=context)


 