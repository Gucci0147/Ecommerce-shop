from django.shortcuts import render
from .models import Contact
from django.contrib import messages
from cart.models import CartItem
# from math import ceil
 
# Create your views here.
def index(request):
    
    if (request.user.is_authenticated):
        total_cart_item = CartItem.objects.filter(user=request.user.id).count()
        return render(request,"index.html",{"total_cart_item": total_cart_item})

    return render(request,"index.html")

def contact(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        desc=request.POST.get("desc")
        pnumber=request.POST.get("pnumber")
        myquery=Contact(name=name,email=email,desc=desc,phonenumber=pnumber)
        myquery.save()
        messages.info(request,"We will get back to you soon..")
    
    if (request.user.is_authenticated):
        total_cart_item = CartItem.objects.filter(user=request.user.id).count()
        return render(request,"contact.html",{"total_cart_item": total_cart_item})

    return render(request, 'contact.html')

def about(request):

    if (request.user.is_authenticated):
        total_cart_item = CartItem.objects.filter(user=request.user.id).count()
        return render(request,"about.html",{"total_cart_item": total_cart_item})
    return render(request, 'about.html')

