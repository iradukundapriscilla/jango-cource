from django.shortcuts import render
from.models import*
# Create your views here.
def home(request):
    return render(request,"index.html")

def crud(request):
    if request.method =="POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        age = request.POST['age']
        phonumber = request.POST['phonumber']

        query = Detail(fname=fname, lname=lname,age=age,phonumber=phonumber)
        query.save()
    return render(request,'crud.html')