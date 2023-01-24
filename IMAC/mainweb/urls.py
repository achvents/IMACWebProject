from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
<<<<<<< Updated upstream
=======
    path('signin/',views.newstaff, name='search_oprec'),
    path('list/',views.staff_form, name='staff_register'),
    path('stafflist/',views.stafflist, name='staff_list'),
    path('delete/<int:id>/',views.staff_delete,name='staff_delete'),
    path('<int:id>/',views.staff_form,name='staff_dataupdate'),
>>>>>>> Stashed changes
]