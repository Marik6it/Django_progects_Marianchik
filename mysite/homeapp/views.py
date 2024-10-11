from django.http import HttpResponse
import html
from django.middleware.csrf import get_token

def home(request):
    content = '<h1> homepage <h1>'\
              '<ul>'\
              '<li> <a href="/hello/Marianchik">Hello</a></li>'\
              '<li> <a href="/calc">Calculator</a></li>'\
              '<li> <a href="/polls">Polls</a></li>'\
              '<li> <a href="getform/"> Guess numbers</a></li>'\
              '</ul>'\


    return HttpResponse(content)

def getform(request):
    response = """
        <p>Impossible GET guessing game...</p>
        <form method="POST">
        <p>
          <label for="guess">Input Guess</label>
          <input type="text" name="Guess" size="40" id="guess"/>
          <input type="hidden" name="csrfmiddlewaretoken" value="__token__"/>
        </p>
          <input type="submit"/>
        </form>"""


    token = get_token(request)
    response = response.replace('__token__', html.escape(token))


    response += dumpdata ('GET', request.GET)
    return HttpResponse(response)

def dumpdata(place, data) :
    retval = ""
    if len(data) > 0 :
        retval += '<p>Incoming '+place+' data:<br/>\n'
        for key, value in data.items():
            retval += html.escape(key) + '=' + html.escape(value) + '</br>\n'
        retval += '</p>\n'
    return retval