from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from about_me.models import (EmailContact, PhoneContact, Myself,
								BackEndCourse, FrontEndCourse,
								Learn,UsefulLinks
							)

# Create your views here.
def home_view(request):
	if request.method=='GET':
		context = {}
		my_info = Myself.objects.latest('updated_at')#.order_by('date_created')
		back_end = BackEndCourse.objects.all()
		fron_end = FrontEndCourse.objects.all()
		learn = Learn.objects.all()
		links = UsefulLinks.objects.all()
		print(my_info)
		print('****** Back end *******')
		print(back_end)
		print('************ Front end******** \n')
		print(fron_end)
		print('************ Learn******** \n')
		print(learn)
		print('************ link******** \n')
		print(links)
		context['my_info']= my_info
		context['back_end']= back_end
		context['front_end']= fron_end
		context['learn']= learn
		context['links']= links
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

