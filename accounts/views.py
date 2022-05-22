from django.http import HttpResponse, HttpRequest

from .models import Information
from .utils import get_client_ip, get_info_by_ip


def home(request: HttpRequest) -> HttpResponse:
    information: dict = {
        "client_ip": get_client_ip(request),
        "user_agent": request.META.get("HTTP_USER_AGENT"),
    }

    if Information.objects.filter(
        client_ip=information["client_ip"]
    ).exists():

        return HttpResponse("Ha mayli")

    additional_info: dict = get_info_by_ip(information["client_ip"])

    Information(**information, **additional_info).save()

    return HttpResponse("Lalala")
