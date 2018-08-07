from django.http import HttpResponse


def problem(request, num):
    return HttpResponse(f"Hello, world: {num}")