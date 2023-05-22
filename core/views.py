from django.shortcuts import render

def box1(request):
    return render(request, 'core/box1.html')

def box2(request):
    return render(request, 'core/box2.html')
