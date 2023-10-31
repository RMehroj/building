from django.contrib import admin
from .models import SalesOffice
from django import forms
from phonenumber_field.widgets import PhoneNumberPrefixWidget

class ContactForm(forms.ModelForm):
    class Meta:
        widgets = {
            'phone': PhoneNumberPrefixWidget(initial='UZB'),
        }

@admin.register(SalesOffice)
class ContactAdmin(admin.ModelAdmin):
    form = ContactForm
