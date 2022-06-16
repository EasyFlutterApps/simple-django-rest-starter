from django.shortcuts import render
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model
from rest_framework.generics import get_object_or_404
from allauth.account.admin import EmailAddress
from allauth.account.utils import send_email_confirmation
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.views import APIView

User = get_user_model()


def email_verified(request):
    print(request.body)
    return render(request, 'email_verified.html', {'user': 'prashant'})

class NewEmailConfirmation(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        user = get_object_or_404(User, email=request.data['email'])

        if email_address := EmailAddress.objects.filter(user=user, verified=True).exists():
            return Response(
                {'message': f'This email: {email_address} is already verified'},
                status=status.HTTP_400_BAD_REQUEST
            )
        try:
            send_email_confirmation(request, user=user)
            return Response(
                {'message': f'Email confirmation sent on {email_address}'},
                status=status.HTTP_201_CREATED
            )
        except APIException:
            return Response(
                {
                    'message': f'''This email {email_address} does not exist,
                                    please create a new account'''
                },
                status=status.HTTP_403_FORBIDDEN
            )
