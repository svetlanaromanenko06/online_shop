from django.shortcuts import render

def shop_home(request):
    return render(request,'catalog/shop_home.html')

def shop_contacts(request):
    return render(request,'catalog/shop_contacts.html')
