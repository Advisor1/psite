from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def home(request):
	context = {}
	return render(request, 'home.html', context)

def about(request):
	context = {}
	return render(request, 'about.html', context)

def consultation(request):
	context = {}
	return render(request, 'consultation.html', context)

def general_insurance(request):
	context = {}
	return render(request, 'general_insurance.html', context)

def life(request):
	context = {}
	return render(request, 'life.html', context)
	
def partners(request):
	context = {}
	return render(request, 'partners.html', context)

def sip(request):
	context = {}
	return render(request, 'sip.html', context)


def contact(request):

	if request.method == 'POST':
		username = request.POST['username']
		useremail = request.POST['useremail']
		usercontact = request.POST['usercontact']
		usermessage = request.POST['usermessage']

		messages.success(request, 'Thanks for your message, we will get back to you soon.')

		send_mail(
		    'message from ' + username, #subject
		    'sender email id : ' +' '+ useremail + '\n \n' + 'User Contact :' + usercontact + '\n \n' + 'Actual message : ' + usermessage, #  message body
		    # from email
		    settings.EMAIL_HOST_USER,
		    ['vikasrajoria11ece@gmail.com'],   #to email
		    fail_silently=False,
			)

		return render(request, 'contact.html', {
			'username' : username,
			})
	else:
		return render(request, 'contact.html', {})