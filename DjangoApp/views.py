from django.shortcuts import render

from django.http import HttpResponse
def index(request):
    return HttpResponse('Hello, World!')
def getname(request):
    str1=input()
    html="<html> Hello  %s </html>" %str1
    return HttpResponse(html)

def template_example(request):
    send={"number1":"15",  "number2":"15",  "result":"30"}
    return render(request,"template1.html",send)