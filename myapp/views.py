from django.shortcuts import render
from  django.http import JsonResponse
# Create your views here.
from myapp.models import contacts
def index(req):
    return render(req,"index.html")

def valid(req):
    return render(req,"validate.html")
    

def reg(req):
    if req.method=='POST':
        name =req.POST.get('name')
        number =req.POST.get('number')
        location =req.POST.get('location')
        abc = contacts(Name=name,PhoneNumber=number,Location=location)
        abc.save()

    return render(req,'reg.html')


def get_contacts(request):
    contact = list(contacts.objects.values())
    return JsonResponse(contact,safe=False)

