from django.core.mail import send_mail
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response


class SendMailView(APIView):
    def get(self, request, *args, **kwargs):
        send_mail(
            'From Demo',  
            'This email from django simple message service', 
            settings.AWS_SES_FROM_EMAIL, 
            ['perezmoon22@gmail.com'], 
        )
        return Response({"message": "Email sent successfully!"})
