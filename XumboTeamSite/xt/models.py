#!/usr/bin/python
# -*- coding: utf8 -*-

from django.db import models

class Member(models.Model):
    #username = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    birthdate = models.DateField()
    url = models.URLField()
    email = models.EmailField()
    photo = models.ImageField(upload_to='profile_images', blank=True)
    def __unicode__(self):
        return unicode(self.name)
    
class News(models.Model):
    title = models.CharField(max_length=100)
    birthdate = models.DateTimeField('Data de publicação: ')
    text = models.TextField()
    def __unicode__(self):
        return unicode(self.title)
    