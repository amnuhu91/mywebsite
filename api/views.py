from django.http import HttpResponse, JsonResponse,Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from datetime  import datetime
from about_me.models import ContactUs, BackEndCourse
from api.serializers import ContactUsSerializer, BackendSerializer, PostSerializer
from blog.models import Post
from blog.send_sms_twilio import send_whatsapp_message

#@csrf_exempt
@api_view(['GET', 'POST'])
def contact_list(request, format=None):
	time = datetime.now()
	if request.method == 'GET':
		contacts = ContactUs.objects.all()
		serializer = ContactUsSerializer(contacts, many=True)
		return JsonResponse(serializer.data, safe=False)
	elif request.method == 'POST':
		#data = JSONParser().parse(request)
		serializer = ContactUsSerializer(data=request.data)
		if serializer.is_valid():
			msg=serializer.save()

			email_smg = f'You have a message from {msg.name} with email: {msg.email}. Message: \"{msg.message}\" on {time.strftime("%d/%m/Y")} at {time.strftime("%I:%M:%S")} '
			send_whatsapp_message(msg=email_smg)
			return Response(serializer.data,status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def contact_detail(request,pk,format=None):
	try:
		contact = ContactUs.objects.get(pk=pk)
	except ContactUs.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)
	if request.method == "GET":
		serializer = ContactUsSerializer(contact)
		return Response(serializer.data)
	elif request.method == 'PUT':
		
		serializer = ContactUsSerializer(contact,data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	elif request.method == "DELETE":
		contact.delete()
		return HttpResponse(status=status.HTTP_204_NO_CONTENT)



class BackendCourseList(APIView):

	def get(self,request,format=None):
		b_courses = BackEndCourse.objects.all()
		serializer = BackendSerializer(b_courses, many=True)
		return Response(serializer.data)

	def post(self,request,format=None):
		serializer = BackendSerializer(data=request.data)
		if serializer.is_valid():
			po = serializer.save()
			
			po.save()
			id = po.id
			course_name = po.course_name
			cstatus = po.status
			date = po.date_added
			message = f'New course {course_name} is added on {date} with status of {cstatus}'
			send_whatsapp_message(msg=message)
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class BackendCourseDetail(APIView):
	def get_object(self,pk):
		try:
			return BackEndCourse.objects.get(pk=pk)
		except BackEndCourse.DoesNotExist:
			raise Http404
	def get(self,request,pk,format=None):
		b_course = self.get_object(pk)
		serializer = BackendSerializer(b_course)
		return Response(serializer.data)

	def put(self,request,pk,format=None):
		b_course = self.get_object(pk)
		serializer = BackendSerializer(b_course, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


	def delete(self,request,pk,format=None):
		b_course = self.get_object(pk)
		b_course.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)


class PostList(APIView):
	authentication_classes = [SessionAuthentication, BasicAuthentication]
	permission_classes = [IsAuthenticated]

	def get(self,request,format=None):
		posts = Post.objects.all()
		serializer = PostSerializer(posts, many=True)
		#print(self.request.user)
		return Response(serializer.data)

	def post(self,request,format=None):
		serializer = PostSerializer(data=request.data)
		if serializer.is_valid():
			post=serializer.save(author=self.request.user)
			#print(self.request.user)
			#print(post.tags)
			message =f'New post with title of \"{post.title}\" is added on {post.publish}'
			send_whatsapp_message(msg=message)
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDetail(APIView):
	authentication_classes = [SessionAuthentication, BasicAuthentication]
	permission_classes = [IsAuthenticated]
	def get_object(self,pk):
		try:
			return Post.objects.get(pk=pk)
		except Post.DoesNotExist:
			raise Http404
	def get(self,request,pk,format=None):
		post = self.get_object(pk)
		serializer = PostSerializer(post)
		return Response(serializer.data)

	def put(self,request,pk,format=None):
		post = self.get_object(pk)
		serializer = PostSerializer(post, data=request.data)
		if serializer.is_valid():
			post=serializer.save(author=self.request.user)
			time = datetime.now()
			message =f'A post with title of \"{post.title}\" is update on {time.strftime("%d/%m/Y")} at { time.strftime("%I:%M:%S")}'
			send_whatsapp_message(msg=message)
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


	def delete(self,request,pk,format=None):
		post = self.get_object(pk)
		time = datetime.now()
		message =f'A post with title of \"{post.title}\" is deleted on {time.strftime("%d/%m/%Y")} at { time.strftime("%I:%M:%S")}'
		send_whatsapp_message(msg=message)
		post.delete()

		return Response(status=status.HTTP_204_NO_CONTENT)
