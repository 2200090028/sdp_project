from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
   # path('admin/', admin.site.urls),
    path('hello/',hello1,name='hello'),
    path('',newhomepage, name='newhomepage'),
    path('travelpackage123/',travelpackage, name='travelpackage123'),
    path('print_to_console/', print_to_console, name='print_to_console'),
    path('p/', print1, name='print1'),
path('randomcall/', randomcall, name='randomcall'),
path('randomlogic/', randomlogic, name='randomlogic'),

path('getdate1/',getdate1,name='getdate1'),
    path('get_date',get_date, name = 'get_date'),

    path('register1/', register1, name='register1'),
    path('registerloginfunction/', registerloginfunction, name='registerloginfunction'),

path('weatherlogic/', weatherlogic, name='weatherlogic'),
path('weatherpagecall/', weatherpagecall, name='weatherpagecall'),

    path('feedback/',feedback,name='feedback'),
    path('feedbackform/',feedbackform,name='feedbackform'),

    path('login/',login,name='login'),
    path('signup/',signup,name='signup'),
path('login1/',login1,name='login1'),
    path('signup1/',signup1,name='signup1'),
    path('logout/',logout,name='logout'),

    ]
