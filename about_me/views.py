from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from about_me.models import EmailContact, PhoneContact, Myself

# Create your views here.
def home_view(request):
	if request.method=='GET':
		context = {}
		my_info = Myself.objects.latest('date_created')#.order_by('date_created')
		print(my_info)
		context['my_info']= my_info
		return render(request, 'about_me/home.html',context)
	return HttpResponse('invalid request')
		
	
	
	

def email_contact_view(request):
	if request.method=='GET':
		data = list(EmailContact.objects.values())
		if len(data) > 0 :
			return JsonResponse(data, safe=False)
		
		return JsonResponse({'data':'No email contact right now'})

def phone_contact_view(request):
	if request.method=='GET':
		data = list(PhoneContact.objects.values())
		if len(data) > 0 :
			return JsonResponse(data, safe=False)
		
		return JsonResponse({'data':'No Phone contact right now'})

