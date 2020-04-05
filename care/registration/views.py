from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Registration
# Create your views here.
def register(request):
    if request.method == 'POST':
        #register user
        #get form values
        firstName = request.POST['first_name']
        lastName = request.POST['last_name']
        phoneNumber = request.POST['phone_number']
        emailAddress = request.POST['email']
        address = request.POST['address']
        city = request.POST['city']
        province = request.POST['province']
        postalCode = request.POST['postal_code']
        # check if the email has been used already. 
        if Registration.objects.filter(emailAddress=emailAddress).exists():
            messages.error(request, "This email is being used")
            return redirect('register')
        else:
            #looks good
            registration = Registration(firstName=firstName, lastName=lastName, phoneNumber=phoneNumber, emailAddress=emailAddress, address=address, city=city, province=province,postalCode=postalCode)
            registration.save()
            messages.success(request, 'You are registered, we will get in touch with you soon!')
            return redirect('register')
    else:
        return render(request, 'registration/registration.html')