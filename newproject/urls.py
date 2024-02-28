from django.urls import path
from .views import *

urlpatterns = [
    path('hello/', hello, name='hello'),
    path('', NewHomePage, name='NewHomePage'),
    path('travel/', TravelPackage, name='TravelPackage'),
    path('print_to_console/', print_to_console, name='print_to_console'),
    path('p/', print1, name='print'),
    path('randomcall/', randomcall, name="randomcall"),
    path('randomlogic/', randomlogic, name="randomlogic"),
    path('getdate1/', getdate1, name="getdate1"),
    path('DateTime/', DateTime, name="DateTime"),
    path('registerlogin/', registerlogin, name='registerlogin'),
    path('registerloginfunction/', registerloginfunction, name='registerloginfunction'),
    path('feedback/', feedback, name='feedback'),
    path('feedbackfunction/', feedbackfunction, name='feedbackfunction'),
    path('pie_chart/', pie_chart, name='pie_chart'),
    path('PieChartForm1/', PieChartForm1, name='PieChartForm1'),
    path('car1/', car1, name='car1'),
    path('weatherpagecall/', weatherpagecall, name='weatherpagecall'),
    path('weatherlogic/', weatherlogic, name='weatherlogic'),
    path('logout/',logout,name='logout'),
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('signup1/', signup1, name='signup1'),
    path('login1/', login1, name='login1'),

]
