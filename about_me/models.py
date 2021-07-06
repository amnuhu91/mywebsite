from django.db import models

# Create your models here.

class PhoneContact(models.Model):
    phone = models.CharField(max_length=14, verbose_name='Phone Number')
    def __str__(self):
        return self.phone


class EmailContact(models.Model):
    email = models.EmailField(verbose_name="email", unique=True)
    def __str__(self):
        return self.email


class Myself(models.Model):
    photo           = models.ImageField(blank=True, null=True)
    brief_article   = models.TextField()
    date_created    = models.DateTimeField(auto_now_add=True, blank=True,null=True)
    updated_at      =models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.brief_article

    class Meta:
        ordering = ['date_created']

class Articles(models.Model):
    title = models.CharField(max_length=150, verbose_name='Article title',blank=True,null=True)
    brief_article   = models.TextField(blank=True,null=True)
    date_created    = models.DateField(auto_now_add=True)
    updated_at      =models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title