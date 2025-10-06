from ckeditor.fields import RichTextField
from django.db import models

# Create your models here.
class Event_speaker(models.Model):
    name = models.CharField(max_length=1000, default="", verbose_name='Familiya Ism Sharif', blank=True, null=True)
    address = models.CharField(max_length=1000, default="", verbose_name='Manzil', blank=True, null=True)
    info = RichTextField()
    img = models.ImageField(upload_to='img/speaker/', blank=True, null=True)
    def __str__(self):
        return self.name

# class Registration(models.Model):
#     prefix = models.CharField(max_length=1000, default="")
#     name = models.CharField(max_length=1000, default="")
#     email = models.EmailField(max_length=1000, default="")
#     phone = models.CharField(max_length=1000, default="")
#     job_title = models.CharField(max_length=1000, default="")
#     affiliated_organization = models.CharField(max_length=1000, default="", )
#     country = models.CharField(max_length=1000, default="", )
#     passport_file = models.FileField(upload_to='file/', )
#     date = models.DateTimeField( blank=True, null=True)
#
#     def __str__(self):
#         return self.name
#     class Meta:
#         verbose_name = "Ro'yxatdan o'tish"
#         verbose_name_plural = "Ro'yxatdan o'tish"

class About(models.Model):
    name = models.CharField(max_length=1000, default="", blank=True, null=True)
    info = RichTextField()
    def __str__(self):
        return self.name


class Sponsor(models.Model):
    name = models.CharField(max_length=1000, default="", blank=True, null=True)
    img = models.ImageField(upload_to='img/sponsor/', blank=True, null=True)
    def __str__(self):
        return self.name

class Partner(models.Model):
    name = models.CharField(max_length=1000, default="", blank=True, null=True)
    img = models.ImageField(upload_to='img/partner/', blank=True, null=True)
    def __str__(self):
        return self.name
class Authors(models.Model):
    name = models.CharField(max_length=1000, default="", blank=True, null=True)
    info = RichTextField()

    def __str__(self):
        return self.name


class Link(models.Model):
    submit_link = models.CharField(max_length=1000, default="", blank=True, null=True)
    register_link = models.CharField(max_length=1000, default="", blank=True, null=True)


