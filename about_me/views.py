from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from about_me.models import (EmailContact, PhoneContact, Myself,
								BackEndCourse, FrontEndCourse,
								Learn,UsefulLinks,FrontEndTopics
							)


#class import
from django.views.generic.detail import DetailView
from django.db.models import Q


# Create your views here.

	
		
	
learn = Learn.objects.all()
links = UsefulLinks.objects.all()	
ext_context={'learn':learn,'links':links}		
#@login_required
def home_view(request):
	if request.method=='GET':
		
		context = {'test':'<h1>hello</h1>'}
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


class FrontCourseDetail(DetailView):
	model = FrontEndCourse
	context_object_name = 'course'


	def get_context_data(self,**kwargs):
		pk= self.kwargs.get('pk')
		context = super().get_context_data(**kwargs)
		context['learn']= Learn.objects.all()
		
		context['links']=  UsefulLinks.objects.all()

		context['ftopics'] =  FrontEndTopics.objects.filter(course_name__exact=pk)
		return context
def search_topic(request,pk):
	course =  FrontEndCourse.objects.all()
	ftopics = FrontEndTopics.objects.filter(course_name__exact=pk)
	result = ftopics
	search_val = request.POST.get('saerch_val')
	if  search_val and  request.method == 'POST':
		qs =  list(FrontEndTopics.objects.filter(Q(course_name__exact=pk) & Q(topic_name__icontains = search_val)).values())
		if  len(qs) >0:
			print(qs)
			result = qs
			return  JsonResponse(result, safe=False)
		return JsonResponse({'result':'no topic found'})
	elif saerch_val =='' and request.method=='POST':
		qs =  list(FrontEndTopics.objects.filter(Q(course_name__exact=pk)).values())
		result=qs
		return  JsonResponse(result, safe=False)
	return render(request, 'about_me/frontendcourse_detail.html',{'course':course,'ftopics':ftopics})
	#return JsonResponse(result, safe=False)
