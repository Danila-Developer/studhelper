from django.urls import path
from .views import index, user_logout

urlpatterns = [
    path('', index),
    path('logout/', user_logout, name='logout')
]