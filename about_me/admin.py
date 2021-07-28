from django.contrib import admin
from about_me.models import (PhoneContact, EmailContact, Myself,
                             Articles, BackEndCourse, FrontEndCourse
                             , Learn, UsefulLinks, FrontEndTopics)

# Register your models here.

class myseladmin(admin.ModelAdmin):
    list_display = ['brief_article','date_created']
    list_editable = ['brief_article']
    list_display_links = None
class BackEndadmin(admin.ModelAdmin):
    list_display = ('course_name','course_desc','date_added','date_updated','status')
    list_editable = ('status',)
    list_display_links =[ 'course_name']
class FrontEndadmin(admin.ModelAdmin):
    list_display=('pk','course_name','course_desc','date_added','date_updated','status')
    list_editable=('status',)
    list_display_links =[ 'course_name']
class Learnadmin(admin.ModelAdmin):
    list_display = ('course_name','course_desc','date_added','date_updated','status')
    #list_editable = ('course_name','course_desc','status')
    list_display_links = ['course_name']
class UsefulLinksadmin(admin.ModelAdmin):
    list_display = ('course_name','course_desc','date_added','date_updated','status')
    #list_editable = ('course_name','course_desc','status')
    list_display_links = ['course_name']
class Phoneadmin(admin.ModelAdmin):
    list_display = ('phone','status')
    list_editable = ('status',)
   
class Emailadmin(admin.ModelAdmin):
    list_display = ('email','status')
    list_editable = ('status',)
class FrontEndTopicsadmin(admin.ModelAdmin):
    list_display = ('course_name','topic_name','topic_desc')
   
admin.site.register(FrontEndTopics, FrontEndTopicsadmin)
admin.site.register(Myself, myseladmin)
admin.site.register(UsefulLinks,UsefulLinksadmin)
admin.site.register(FrontEndCourse, FrontEndadmin)
admin.site.register(BackEndCourse, BackEndadmin)
admin.site.register(Learn, Learnadmin)
admin.site.register(Articles)
admin.site.register(EmailContact, Emailadmin)
admin.site.register(PhoneContact,Phoneadmin)