from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods

from .models import Messages


def main(request):
	return render(request, 'main.html')

def contact(request):
  if request.method == 'POST':
    name = request.POST.get('name')
    email = request.POST.get('email')
    discord = request.POST.get('discord')
    message = request.POST.get('message')
    Messages.objects.create(name=name, email=email, message=message)

    try:
      send_mail(
        f'New message from {name}',
        f'Email: {email}, Message: {message}, DC: {discord}',
        settings.EMAIL_HOST_USER,
        ['fraanab.oml@gmail.com'],
        fail_silently=False,
      )
    except Exception as e:
      messages.error(request, f'Error sending message {str(e)}')
    return JsonResponse({'message': "Message sent successfully!", "style":"color: #0c0"})
  return render(request, 'contact.html')
