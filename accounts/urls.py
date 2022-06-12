from django.urls import path

from .views import NewEmailConfirmation

urlpatterns = [
    path('resend-verification-email/', NewEmailConfirmation.as_view(),
         name='resend-email-confirmation'),

]
