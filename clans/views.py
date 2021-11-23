from django.shortcuts import render
from .models import Contact

from django.http import HttpResponse

# Create your views here.
def contact(request):
    thank = False
    if request.method=="POST":
        name = request.POST.get('name', '')
        admission = request.POST.get('admission', '')
        email = request.POST.get('email', '')
        gender = request.POST.get('gender', '')
        phone = request.POST.get('phone', '')
        contact = Contact(name=name, email=email, phone=phone, gender=gender, admission=admission)
        contact.save()
        thank = True
        if thank:
            return render(request, 'contact.html',{'thank': thank})
    return render(request, 'contact.html',{'thank': thank})

def thanks(request):
    return render(request, 'thanks.html')
