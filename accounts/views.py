from django.shortcuts import render
from .models import Information
from django.http import HttpResponse


def home(request):
    def get_client_ip(request):
        x = request.META.get('HTTP_X_FORWARDED_FOR')
        if x:
            ip = x.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
    client_address = request.META.get("HTTP_USER_AGENT")
    inf = Information()
    if request.user.is_authenticated:
        inf.user = request.user
    inf.client = client_address
    inf.ip = get_client_ip(request)
    inf.save()
    return HttpResponse("Lalala")
