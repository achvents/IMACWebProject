from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import member, IMACevents, article

admin.site.register(member, UserAdmin)
admin.site.register(IMACevents)
admin.site.register(article)

