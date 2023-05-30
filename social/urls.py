from django.urls import path
from . import views

app_name ='Twitt'
urlpatterns = [
    path('',views.home,name='home'),
    path('profile/list/',views.profilelist,name="profilelist"),
    path('profile/<int:pk>',views.profile,name='profile'),
    path ('logsin/',views.logsin,name='logsin'),
    path('logout/',views.logsout,name='logsout'),
    path('register/',views.registeruser,name='registeruser'),
    path('edituserinfo/',views.edit_user_info,name='editeuserinfo'),
    path('change_password/',views.changepassword,name='password_change'),
    path('updateprofilepic/',views.edit_pic,name='updateprofilepic'),
    path('like_twitt/<int:pk>/',views.like_twitt,name='like_twitt'),
    path('twitt/',views.individoual_twitt,name='individoual_twitt'),
]
