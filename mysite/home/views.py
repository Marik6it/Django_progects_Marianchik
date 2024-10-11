from django.http import HttpResponse

def hello(request):
    content = "<h1> homepage <h1>"\
              "<ul>"\
              "<li>Text</li>"\
              "</ul>"
    return HttpResponse(content)