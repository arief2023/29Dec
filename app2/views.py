from django.shortcuts import render

# Create your views here.
def user(request):
    d={'user':'Django'}
    return render(request,'user.html',context=d)