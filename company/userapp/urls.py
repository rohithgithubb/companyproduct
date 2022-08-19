from unicodedata import name
from django.urls import path
from.import views

urlpatterns = [
    path('',views.home,name="home"),
    path('register',views.reg,name='register'),
    path('logpage',views.logpage,name='loginn'),
    path('loged',views.logacc,name="loged"),
    path('proadd',views.pro_add,name="add"),
    path('del',views.productdel),
    path('productupdate',views.productup)
]