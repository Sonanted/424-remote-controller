from django.urls import path
from .views import *
urlpatterns = [
    path('', home_page, name='home'),
    path('oscilloscope/', Scope.as_view(), name='scope'),
    path('login/', login_page, name='login'),
    path('logout/', logout_page, name='logout'),
    path('pass_reset', reset_page, name='password_reset'),
]
