# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 16:37:55 2015

@author: fansh_000
"""
from django.template import Context
from django.shortcuts import render_to_response
from models import *
from django.http import HttpResponseRedirect

def showbooks(request):
    book_list = Book.objects.all()
    c = Context({"book_list": book_list})
    return render_to_response("search_by_author.html", c)
def deletebook(request):
    dltid = request.GET["id"]
    Book.objects.filter(id=dltid).delete()
    return HttpResponseRedirect("/search_by_author")
def showbooks2(request):
    shoid = request.GET["id"]
    book = Book.objects.get(id=shoid)
    author = book.author    
    publisher = book.publisher
    c = Context({"book": book,"author": author,"publisher":publisher})
    return render_to_response("show_book.html", c)
def searchbook(request):
    autname = request.GET["words"]
    authors = Author.objects.get(name=autname)
    book_list = Book.objects.filter(author=authors)
    #book_list = Book.objects.filter(author.name=autname)
    c = Context({"book_list": book_list,"author_name":authors.name})
    return render_to_response("show_author_books.html", c)
    
    
    
    
    
    
    
    
    
    
    
    
