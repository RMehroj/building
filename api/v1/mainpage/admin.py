from django.contrib import admin
from .models import SalesOffice, Apartment, Projects, SocialNetwork, Newsroom, About
from django import forms
from phonenumber_field.widgets import PhoneNumberPrefixWidget

class ContactForm(forms.ModelForm):
    class Meta:
        widgets = {
            'phone': PhoneNumberPrefixWidget(initial='UZB'),
        }

@admin.register(SalesOffice)
class SalesOfficeAdmin(admin.ModelAdmin):
     form = ContactForm

@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    pass


@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    pass


@admin.register(SocialNetwork)
class SocialNetworkAdmin(admin.ModelAdmin):
    pass


@admin.register(Newsroom)
class NewsroomAdmin(admin.ModelAdmin):
    pass


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    pass

