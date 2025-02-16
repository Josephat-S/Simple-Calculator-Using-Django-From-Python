from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request,'index.html')

def operation(request):
    val1 = int(request.GET["num1"])
    val2 = int(request.GET["num2"])

    operator = request.GET["operator"]

    if(operator == '+'):
        res = val1 + val2
        return render(request,'index.html',{'result': res})
    elif(operator == '-'):
        res = val1 - val2
        return render(request,'index.html',{'result': res})
    elif(operator == '*'):
        res = val1 * val2
        return render(request,'index.html',{'result': res})
    elif(operator == '%'):
        res = val1 % val2
        return render(request,'index.html',{'result': res})
    elif(operator == '/'):
        if(val2 != 0):
            res = val1 / val2
            return render(request,'index.html',{'result': res})
        else:
            print("Invalid operation")
    else:
        print("Invalid input!")
