from django.contrib import admin
from api.models import ContactForm

# Register your models here.

class AdminContactForm(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone','father','school','aducation','message')

admin.site.register(ContactForm, AdminContactForm)