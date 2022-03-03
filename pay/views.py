from django.shortcuts import redirect, render
import autopayment
from django.conf import settings
from .models import packages, payment_num
from .form import Payform
from django.contrib import messages

#stripe.api_key = settings.STRIPE_SECRET_KEY


def LandingPageView(request):
    # phone_num= request.POST.get('phone_num')
    # saverecord = payment_num(phone_num=phone_num)
    # saverecord.save()
    # messages.success(request, 'Record saved successfully')

    pkg = packages.objects.all() #getting  info from the database
    if request.method == 'POST' :
        phone = request.POST['phone']  
        saverecord = payment_num(phone_num = phone) 
        saverecord.save()

    #    if request.POST.get('phone_num'):
    #        saverecord = phone_num= request.POST.get('phone_num')
    #        saverecord.phone_num= request.POST.get('phone_num')
    #        if saverecord.is_valid():
    #            saverecord.save()  
    #        messages.success(request, 'Record saved successfully')      

       
    return render(request, 'landing.html',{'pkg' : pkg})

    

# def Checkout(request):
#     if request.method == 'POST':
#         form = Payform(request.POST)
#         if form.is_valid():
#             form.save()
#     form = Payform()
#     return render(request,'/', {'form': form})

# def pay(request):
#     return redirect(request,'checkout')

# class LandingPageView(TemplateView):
#     temlate_name = '/templates/landing.html'

# def cancle(request):
#     autopayment.cancle(request)
    # return redirect('/')
