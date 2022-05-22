import requests
from django.http import HttpRequest


IP_API_URL: str = "https://ipapi.co/{ip}/json"


def get_client_ip(request: HttpRequest) -> str:
    http_x: str = request.META.get('HTTP_X_FORWARDED_FOR')

    if http_x:
        return http_x.split(',')[0]

    return request.META.get('REMOTE_ADDR')


def get_info_by_ip(client_ip: str) -> dict:
    response: dict = requests.get(
        IP_API_URL.format(ip=client_ip)
    ).json()

    return {
        "city": response.get("city"),
        "org": response.get("org")
    }
