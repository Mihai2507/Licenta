from django.urls import path
from django.contrib.auth import views as auth_views
from .views import user_login, user_logout

urlpatterns = [
    path('', user_login, name='login'),
    path('logout/', user_logout, name='logout'),

    # Resetare parolă
    path('forgot-password/', auth_views.PasswordResetView.as_view(template_name='forgot_password.html'), name='password_reset'),
    path('forgot-password/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
]
