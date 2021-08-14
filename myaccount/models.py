from django.db import models


from django.contrib.auth.models import AbstractBaseUser, BaseUserManager






class MyAccountManager(BaseUserManager):
	def create_user(self, email,  password=None):
		if not email:
			raise ValueError('Users must have an email address')
		

		user = self.model(
			email=self.normalize_email(email),
			
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_staffuser(self, email, password):
		# """
		# Creates and saves a staff user with the given email and password.
		# """
		user = self.create_user(
            email,
            password=password
        )
		user.staff = True
		user.save(using=self._db)
		return user

	def create_superuser(self, email,  password):
		user = self.create_user(
			email=self.normalize_email(email),
			password=password
			
		)
		user.admin = True
		user.staff = True
		user.superuser = True
		user.save(using=self._db)
		return user


class Account(AbstractBaseUser):
	objects = MyAccountManager()
	email 					= models.EmailField(verbose_name="email address", max_length=60, unique=True)
	#username 				= models.CharField(max_length=30, unique=True)
	other_name 				= models.CharField(max_length=30, blank=True, null =True, verbose_name='other name(s)')
	last_name 				= models.CharField(max_length=30, blank=True, null =True, verbose_name='last name')
	first_name 				= models.CharField(max_length=30, blank=True, null =True, verbose_name='first name')
	date_joined				= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
	last_login				= models.DateTimeField(verbose_name='last login', auto_now=True)
	img           			= models.ImageField(default='cancer.jpg')
	admin				= models.BooleanField(default=False)
	is_active				= models.BooleanField(default=True)
	staff				= models.BooleanField(default=False)
	superuser			= models.BooleanField(default=False)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []

	objects = MyAccountManager()

	def __str__(self):
		return self.email

	# # For checking permissions. to keep it simple all admin have ALL permissons
	# def has_perm(self, perm, obj=None):
	# 	return self.is_admin

	# # Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
	# def has_module_perms(self, app_label):
	# 	return True


	def get_full_name(self):
		# The user is identified by their email address
		return self.email

	def get_short_name(self):
		 # The user is identified by their email address
		 return self.email

	def __str__(self):
		 return self.email

	def has_perm(self, perm, obj=None):
		# "Does the user have a specific permission?"
		# Simplest possible answer: Yes, always
		return True

	def has_module_perms(self, app_label):
		#"Does the user have permissions to view the app `app_label`?"
		# Simplest possible answer: Yes, always
		return True

	@property
	def is_staff(self):
		#"Is the user a member of staff?"
		return self.staff

	@property
	def is_admin(self):
		# "Is the user a admin member?"
		return self.admin
	@property
	def is_superuser(self):
		# "Is the user a admin member?"
		return self.superuser




	
	
