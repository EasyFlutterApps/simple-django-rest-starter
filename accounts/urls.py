from django.urls import path

# from accounts.views import NewEmailConfirmation, email_verified
from accounts import views

urlpatterns = [
    path('resend-verification-email/', views.NewEmailConfirmation.as_view(),
         name='resend-email-confirmation'),

    path('email-verified/', views.email_verified, name='email-verified'),
]
