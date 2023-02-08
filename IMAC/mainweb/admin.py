from django.contrib import admin
from .models import IMACevents, article, User, Nama_Manajer, Divisi
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

#Kalo bikin model baru jangan lupa masukin sini yaa (Register dibawah)
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password', 'name', 'last_login','nrp','IMACid','usergroup')}),
        ('Permissions', {'fields': (
            'is_active', 
            'is_staff', 
            'is_superuser',
            'groups', 
            'user_permissions'
        )}),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('IMACid','email','name', 'password1', 'password2','groups', 'nrp','usergroup')
            }
        ),
    )

    list_display = ('email', 'name', 'is_staff', 'last_login')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)


admin.site.register(User, UserAdmin)

admin.site.register(IMACevents)
admin.site.register(article)
admin.site.register(Divisi)
admin.site.register(Nama_Manajer)