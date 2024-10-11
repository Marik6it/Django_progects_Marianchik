from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, Marianchik! You're at the polls index.")