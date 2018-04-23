from django.shortcuts import render
from django.template import loader

# Create your views here.

def index(request):
    return render(request, 'taquin/index.html')

def compute(request):
    import pdb; pdb.set_trace()    