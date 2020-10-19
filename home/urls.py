from django.urls import path
from . import views


urlpatterns = [
path('', views.home, name='home'),
path('login', views.login, name='login'),
path('register', views.register, name='register'),
path('regdata', views.reg_data, name='regdata'),
path('logdata', views.log_data, name='logdata'),
path('loghome', views.log_home, name='loghome'),
path('loggout', views.logg_out, name='loggout'),
path('bookreg', views.book_reg, name='bookreg'),
path('bookdis', views.book_dis, name='bookdis'),
path('submit', views.submitted, name='submit'),
path('bookrec', views.book_rec, name='bookrec'),
]