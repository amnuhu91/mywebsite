from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from about_me.models import ContactUs
from api.serializers import ContactUsSerializer


@csrf_exempt
def contact_list(request):
	if request.method == 'GET':
		contacts = ContactUs.objects.all()
		serializer = ContactUsSerializer(contacts, many=True)
		return JsonResponse(serializer.data, safe=False)
	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = ContactUsSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data,status=201)
		return JsonResponse(serializer.errors, status=400)
@csrf_exempt
def contact_detail(request,pk):
	try:
		contact = ContactUs.objects.get(pk=pk)
	except ContactUs.DoesNotExist:
		return HttpResponse(status=404)
	if request.method == "GET":
		serializer = ContactUsSerializer(contact)
		return JsonResponse(serializer.data)
	elif request.method == 'PUT':
		data = JSONParser().parse(request)
		serializer = ContactUsSerializer(contact,data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data)
		return JsonResponse(serializer.errors,status=400)
	elif request.method == "DELETE":
		contact.delete()
		return HttpResponse(status204)