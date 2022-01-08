from django.urls import path
from django.urls.conf import include 
from . import views


urlpatterns = [
    path('',views.home , name='home'),
    path('category/<str:k>',views.category,name = 'category'),
    path('/language/<str:k>',views.language,name = 'language'),
    path('/country/<str:k>',views.category,name = 'country')
]