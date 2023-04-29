from django.shortcuts import render
from django.http import HttpResponse
tax_rate = 15
def firstView(request):
    return render(request, "taxes/labx.html")
def secondView(request, num):
    num = num + (tax_rate/100*num)
    return HttpResponse(num)
def thirdView(request):
    return render(request,"taxes/taxRate.html", {"tax_rate":tax_rate})
# Create your views here.
