# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 16:38:27 2015

@author: fansh_000
"""
from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=30)


class Author(models.Model):
    name = models.CharField(max_length=30)
    city = models.CharField(max_length=30)

class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.CharField(max_length=30)
    price = models.CharField(max_length=5)
    
