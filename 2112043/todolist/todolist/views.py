from django.http import HttpResponse

def about(request):
    return HttpResponse('<p>Halaman About</p>')