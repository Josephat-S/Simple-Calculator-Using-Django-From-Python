from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# Creating a method for calling index page
def home(request):
    return render(request,'index.html')
# function for checking the operator and display the result
def operation(request):
# Fetching variables
    val1 = int(request.GET["num1"])
    val2 = int(request.GET["num2"])
# Fetching the operator
    operator = request.GET["operator"]
# Checking the operator and performing the operation
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
