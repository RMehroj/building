from django.db import models
from location_field.models.plain import PlainLocationField

class Projects(models.Model):
    uuid = models.UUIDField()
    title = models.CharField()
    apartment = models.IntegerField()
    parking = models.IntegerField()
    price = models.ImageField()
    video = models.FileField()
    text = models.TextField()
    start_date = models.DateField()
    finsh_date = models.DateField()
    created_at = models.DateTimeField()
    update_at = models.DateTimeField()


class SocialNetwork(models.Model):
    title = models.CharField()
    instagram = models.URLField()
    telegram = models.URLField()
    facebook = models.URLField()


class SalesOffice(models.Model):
    uuid = models.UUIDField()
    project_title = models.ForeignKey(Projects)
    social_network = models.ForeignKey(SocialNetwork)
    phone = models.Phonenumber()
    location = PlainLocationField()
    created_at = models.DateTimeField()
    update_at = models.DateTimeField()


class Newsroom(models.Model):
    uuid = models.UUIDField()
    title = models.CharField()
    text = models.TextField()
    image = models.ImageField()
    created_at = models.DateTimeField()
    update_at = models.DateTimeField()


class About(models.Model):
    uuid = models.UUIDField()
    company_name = models.CharField()
    license = models.ImageField()
    achievements = models.ImageField()
    phone = models.Phonenumber()
    about = models.TextField()
    created_at = models.DateTimeField()
    update_at = models.DateTimeField()