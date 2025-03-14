from django.urls import path
from .views import signup, activate

urlpatterns = [
    path('', signup, name='signup'),
    path('activate/<int:user_id>/', activate, name='activate'),
]
