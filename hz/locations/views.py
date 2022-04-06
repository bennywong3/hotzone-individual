from django.shortcuts import render
import requests
from .models import Geodata

def getgeodata(request):
    geodata = {'nameEN':'','addressEN':'','x':'','y':''}
    if 'userinput' in request.GET:
        userinput = request.GET['userinput']
        url = 'https://geodata.gov.hk/gs/api/v1.0.0/locationSearch?q=%s' % userinput
        response = requests.get(url)
        if response.status_code == requests.codes.ok:
            j = response.json()
            geodata = j[0]
            name2=geodata['nameEN']
            address2=geodata['addressEN']
            Xcoor2=geodata['x']
            Ycoor2=geodata['y']

            Geodata.objects.create(name=name2, address=address2, Xcoor=Xcoor2, Ycoor= Ycoor2)
    return render(request, 'input.html', {
        'name2': geodata['nameEN'],
        'address2': geodata['addressEN'],
        'Xcoor2': geodata['x'],
        'Ycoor2': geodata['y']
    })
