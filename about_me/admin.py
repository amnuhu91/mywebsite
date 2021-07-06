from django.contrib import admin
from about_me.models import PhoneContact, EmailContact, Myself, Articles

# Register your models here.

class myseladmin(admin.ModelAdmin):
    list_display = ['brief_article','date_created']
admin.site.register(Myself, myseladmin)
admin.site.register(Articles)
admin.site.register(EmailContact)
admin.site.register(PhoneContact)