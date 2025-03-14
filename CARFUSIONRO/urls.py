from django.contrib import admin
from django.urls import include, path
from login.views import user_logout
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', include('signup.urls')),
    path('login/', include('login.urls')),
    path('logout/', user_logout, name='logout'),
    path('profil/', include('profil.urls')),
    path('admin/', admin.site.urls),
    path('send-message/', views.send_message, name='send_message'),
    path('adauga/', include('sellcar.urls')),
]
