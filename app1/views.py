from django.shortcuts import render

# Create your views here.
def jinja_print(request):
    D={'Name':'Arief','Age':22,'Mobile':[8686878382]}
    return render(request,'jinja_print.html',context=D)