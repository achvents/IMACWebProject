from django.shortcuts import render, redirect
from .models import IMACevents, article, member
from .forms import StaffForm
from .models import staff_imac
from django.contrib.auth import authenticate, login


def home(request):
    num_member = member.objects.all().count()
    num_events = IMACevents.objects.all().count()
    num_article = article.objects.all().count()

    context = {
        'num_member': num_member,
        'num_events': num_events,
        'num_article': num_article,
    }

<<<<<<< Updated upstream
    return render(request, 'home.html', context=context)
=======
    return render(request, 'home.html', context=context)


# buat error ini yang fix bisa jalan
def handle_not_found(request, exception):
    return render(request, "error.html")

# data data titit

# buat nunjukin list staff


def stafflist(request):
    context = {'stafflist': staff_imac.objects.all()}
    return render(request, "mainweb/stafflist.html", context)


# buat masukin data staff
def staff_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = StaffForm()
        else:
            staff = staff_imac.objects.get(pk=id)
            form = StaffForm(instance=staff)
        return render(request, "mainweb/staff_form.html", {'form': form})
    else:
        if id == 0:
            form = StaffForm(request.POST)
        else:
            staff = staff_imac.objects.get(pk=id)
            form = StaffForm(request.POST, instance=staff)
        if form.is_valid():
            form.save()
    return redirect('/home/stafflist')


def staff_delete(request, id=0):
    staff = staff_imac.objects.get(pk=id)
    staff.delete()
    return redirect('/home/stafflist')


def newstaff(request):

    if request.method == 'POST':
        nrp = request.POST['nrp']

        user = authenticate(nrp=staff_imac.nrp)

        if user is not None:
            login(request, user)
            nrp = staff_imac.nrp
            return render(request, "mainweb/welcome.html", {'nrp': nrp})
        else:
            messages.error(request,"Yha gagal kenthu")
            return redirect('/home')

    return render(request,"mainweb/newstaff.html")
    
>>>>>>> Stashed changes
