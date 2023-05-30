from django.contrib import admin
from .models import Profile,Twitt
from django.contrib.auth.models import User,Group

class ProfileInLine(admin.StackedInline):
    model = Profile

class UerAdmin(admin.ModelAdmin):
    model = User
    fields=['username','password']
    inlines = [ProfileInLine]


admin.site.unregister(Group)
admin.site.unregister(User)
admin.site.register(User,UerAdmin)
admin.site.register(Twitt)
