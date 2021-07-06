from django.contrib import admin
from about_me.models import (PhoneContact, EmailContact, Myself,
                             Articles, BackEndCourse, FrontEndCourse
                             , Learn, UsefulLinks)

# Register your models here.

class myseladmin(admin.ModelAdmin):
    list_display = ['brief_article','date_created']
class BackEndadmin(admin.ModelAdmin):
    list_display = ('course_name','course_desc','date_added','date_updated')
class FrontEndadmin(admin.ModelAdmin):
    list_display=('course_name','course_desc','date_added','date_updated')
class Learnadmin(admin.ModelAdmin):
    list_display = ('course_name','course_desc','date_added','date_updated')
class UsefulLinksadmin(admin.ModelAdmin):
    list_display = ('course_name','course_desc','date_added','date_updated')

admin.site.register(Myself, myseladmin)
admin.site.register(UsefulLinks,UsefulLinksadmin)
admin.site.register(FrontEndCourse, FrontEndadmin)
admin.site.register(BackEndCourse, BackEndadmin)
admin.site.register(Learn, Learnadmin)
admin.site.register(Articles)
admin.site.register(EmailContact)
admin.site.register(PhoneContact)