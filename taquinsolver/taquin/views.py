from django.shortcuts import render
from django.template import loader
from django.http import JsonResponse

# Create your views here.

def index(request):
    return render(request, 'taquin/index.html')

def compute(request):
    initial = ['i-one', 'i-two', 'i-three', 'i-four', 'i-five', 'i-six', 'i-seven', 'i-eight', 'i-nine']
    target = ['t-one', 't-two', 't-three', 't-four', 't-five', 't-six', 't-seven', 't-eight', 't-nine']
    init_list = []
    target_list = []
    for i in initial:
        init_list.append(request.POST[i])
    for j in target:
        target_list.append(request.POST[j])
    print(target_list, init_list)
    return JsonResponse({'init': init_list, 'target': target_list})