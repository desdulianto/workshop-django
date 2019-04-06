from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):

    name = request.GET.get('name', 'World')
    context = dict(name=name)
    return render(request, 'hello/index.html', context)

def bye(request):
    return HttpResponse('Bye-bye world')
