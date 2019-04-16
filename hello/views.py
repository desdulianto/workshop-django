from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect

from .forms import HelloForm

def index(request):
    if request.method == 'POST':
        form = HelloForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name', 'World')
            pilihan = form.cleaned_data.get('pilihan', 'hello')
            url = 'hello_{}'.format(pilihan)
            return HttpResponseRedirect(
                    '{}?name={}'.format(reverse(url), name))
        return render(request, 'hello/form.html', {'form': form})
    form = HelloForm()
    return render(request, 'hello/form.html', {'form': form})

def hello(request):
    name = request.GET.get('name', 'World')
    name = 'World' if name.strip() == '' else name
    return render(request, 'hello/index.html',
            {'name': name, 'greeting': 'Hello'})

def bye(request):
    name = request.GET.get('name', 'World')
    name = 'World' if name.strip() == '' else name
    return render(request, 'hello/index.html',
            {'name': name, 'greeting': 'Bye-bye'})
