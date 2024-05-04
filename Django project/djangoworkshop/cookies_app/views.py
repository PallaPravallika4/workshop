from django.http import HttpResponse

def set_cookie(request):
    response = HttpResponse("Cookie set!")
    response.set_cookie('username', 'pravallika')

    return response

def get_cookie(request):
    username = request.COOKIES.get('username', 'Guest')
    return HttpResponse(f"Hello, username !")
