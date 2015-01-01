from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Scene(models.Model):
	name = models.CharField(max_length=200)
	desc = models.CharField(max_length=200,null = True, blank=True)

	def __unicode__(self):
		return self.name

class Package(models.Model):
	scene = models.ForeignKey(Scene)
	furniture = models.CharField(max_length=200, null=True, blank=True)

	def __unicode__(self):
		return self.scene

class Furniture_category(models.Model):
	name = models.CharField(max_length=200)
	desc = models.CharField(max_length=200)
	def __unicode__(self):
		return self.name

class Furniture(models.Model):
	name = models.CharField(max_length=200)
	category = models.ForeignKey(Furniture_category)
	sold_by = models.CharField(max_length=200)
	Width = models.CharField(max_length=200, null=True, blank=True)
	Depth = models.CharField(max_length=200, null=True, blank=True)
	Height = models.CharField(max_length=200, null=True, blank=True)
	Color = models.CharField(max_length=200, null=True, blank=True)
	Materials = models.CharField(max_length=200, null=True, blank=True)
	Designer = models.CharField(max_length=200, null=True, blank=True)
	Category = models.CharField(max_length=200, null=True, blank=True)
	Style = models.CharField(max_length=200, null=True, blank=True)
	active = models.BooleanField(default=True)

	def __unicode__(self):
		return self.name



class UserProfile(models.Model):
    user = models.OneToOneField(User,related_name='user_profile')
    description = models.CharField(max_length=128, null= True,blank=True)
    facebook_id = models.CharField(max_length=128, null = True,blank=True)
    gender = models.CharField(max_length=128, null = True,blank=True)

    def __unicode__(self):
        return self.user.username

