from rest_framework import serializers
from about_me.models import ContactUs, BackEndCourse





class ContactUsSerializer(serializers.ModelSerializer):
	class Meta:
		model = ContactUs
		fields = '__all__'
	# id = serializers.IntegerField(read_only=True)
	# name = serializers.CharField(required=False, max_length=200,allow_blank=True)
	# email = serializers.EmailField(required=False, allow_blank=True, max_length=200)
	# email = serializers.CharField(required=False,allow_blank=True, max_length=500)

	# def create(self,validated_data):
	# 	return ContactUs.objects.create(**validated_data)

class BackendSerializer(serializers.ModelSerializer):
	class Meta:
		model = BackEndCourse
		fields = '__all__'

