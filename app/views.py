from django.shortcuts import render

# Create your views here.
from app.models import *
def display_country(request):
    qlco=Country.objects.all()
    d={'country':qlco}
    return render(request,'display_country.html',d)



def display_capital(request):
    qlco=Capital.objects.all()
    d={'capital':qlco}
    return render(request,'display_capital.html',d)



def insert_country(request):
    co=input('enter country_id')
    cn=input('enter country_name')  
    cl=input('enter c_language')
    COU=Country.objects.get_or_create(country_id=co,country_name=cn,c_language=cl)[0]
    COU.save()

    qlco=Country.objects.all()
    d={'country':qlco}
    return render(request,'display_country.html',d)


def insert_capital(request):
    ca=input('enter capital_id')
    can=input('enter capital_name')
    co=input('enter country_id')
    CO=Country.objects.get(country_id=co)
    CAO=Capital.objects.get_or_create(country_id=CO,capital_name=can,capital_id=ca)[0]
    
    qlco=Capital.objects.all()
    d={'capital':qlco}
    return render(request,'display_capital.html',d)

