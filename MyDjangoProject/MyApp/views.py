from django.shortcuts import render, HttpResponse
from datetime import datetime
from MyApp.models import Contact
# Create your views here.
def index(request):
    return render(request,'index.html')
    #return HttpResponse("Hello World , HomePage")

def about(request):
    return HttpResponse("Hello World, About Page")

def contact(request):
    #return HttpResponse("Hello World , Contact")
    if request.method == "POST":
        name1 =request.POST.get('name')
        email1 =request.POST.get('email')
        phone1 =request.POST.get('phone')
        msg1 =request.POST.get('msg')
        date1 = datetime.now()
        formdata = Contact(name=name1,email=email1,phone=phone1,msg=msg1,date=date1)
        formdata.save()
    return render(request,'contact.html')