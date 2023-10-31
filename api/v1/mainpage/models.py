import uuid
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 

from location_field.models.plain import PlainLocationField
from phonenumber_field.modelfields import PhoneNumberField


class Apartment(models.Model):
    uuid = models.UUIDField(
        primary_key = True, 
        default = uuid.uuid4, 
        editable = False
        )
    apartment = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10000)])
    floor = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    parking = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(1000)])
    price = models.ImageField(upload_to='static/static_dirs/images/price/')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Aparttment'

    def __str__(self):
        return str(self.uuid)


class Projects(models.Model):
    uuid = models.UUIDField(
        primary_key = True, 
        default = uuid.uuid4, 
        editable = False
        )
    title = models.CharField(max_length=512)
    apartments = models.ManyToManyField(Apartment, related_name="projects")
    image = models.ImageField(upload_to='static/static_dirs/images/projects/')
    description = models.TextField()
    finish_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Projects'

    def __str__(self):
        return self.title


class SocialNetwork(models.Model):
    title = models.CharField(max_length=255)
    instagram = models.URLField(max_length=200)
    telegram = models.URLField(max_length=200)
    facebook = models.URLField(max_length=200)

    class Meta:
        db_table = 'SocialNetwork'

    def __str__(self):
        return self.title


class SalesOffice(models.Model):
    uuid = models.UUIDField(primary_key = True, 
         default = uuid.uuid4, 
         editable = False)
    projects = models.ForeignKey(
        Projects, 
        on_delete=models.CASCADE
        )
    social_network = models.ForeignKey(
        SocialNetwork, 
        on_delete=models.CASCADE
        )
    phone = PhoneNumberField()
    city = models.CharField(
        max_length=255
        )
    location = PlainLocationField(
        based_fields=['city'],
        zoom=7
        )
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'SalesOffice'

    def __str__(self):
        return self.projects


class Newsroom(models.Model):
    uuid = models.UUIDField(
        primary_key = True, 
        default = uuid.uuid4, 
        editable = False
        )
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='static/static_dirs/images/newsroom/')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Newsroom'

    def __str__(self):
        return self.title


class About(models.Model):
    uuid = models.UUIDField(
        primary_key = True, 
        default = uuid.uuid4, 
        editable = False
        )
    company_name = models.CharField(max_length=255)
    license = models.ImageField(
        upload_to='static/static_dirs/images/license/'
        )
    achievements = models.ImageField(
        upload_to='static/static_dirs/images/achievements/'
        )
    phone = PhoneNumberField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'About'

    def __str__(self):
        return self.company_name