from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('show',views.show),
    path('signup',views.signup_view,name='signup'),
    path('saveSignup',views.saveSignup),
    path('login/',views.login_view),
    path('cart',views.cart_view),
    path('savecart',views.savecart_view),
    path('relate',views.relate_view),
     path('login/show',views.show),

 ] 
