from django.db import models
from django.urls import reverse ,reverse_lazy

# Create your models here.


class Blog(models.Model):
    title = models.SlugField(max_length=200,null = True, blank=True)
    body = models.TextField(null = True, blank=True)
    image = models.ImageField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    viewable = models.BooleanField(default=True)
    comment = models.TextField(null = True, blank=True)
    class Meta:
        ordering =['-updated_on']
    def __str__(self):
        return self.title
    # def get_absolute_url(self):
    #     return reverse_lazy('add-blog/')
