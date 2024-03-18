from django.http import HttpResponse


def index(request): # noqa: ARG001
    return HttpResponse(b"Hello, world. You're at the polls index.")
