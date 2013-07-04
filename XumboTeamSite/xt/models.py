#!/usr/bin/python
# -*- coding: utf8 -*-

from django.db import models
from datetime import datetime   

class Member(models.Model):
    #username = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    birthdate = models.DateField()
    url = models.URLField(blank=True)
    email = models.EmailField(blank=True)
    photo = models.ImageField(upload_to='profile_images', blank=True)
    def __unicode__(self):
        return unicode(self.name)
    
class Image(models.Model):
    photo = models.ImageField(upload_to='images')
    date_uploaded=models.DateTimeField(default=datetime.now())
    title=models.CharField(max_length=300, blank=True)
    description=models.TextField(blank=True)
    def __unicode__(self):
        return unicode(self.photo) #modificar para ter timestamp?
    
class News(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Data de publicação: ')
    text = models.TextField()
    images=models.ManyToManyField(Image)
    def __unicode__(self):
        return unicode(self.title)
    