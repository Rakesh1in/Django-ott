from django.urls import path
from accounts_app.views import fun_login, fun_register, fun_logout

urlpatterns = [
    path("",fun_login,name='go_login'),
    path("register",fun_register, name='go_register'),
    path("logout",fun_logout, name='go_logout'),
    
]


