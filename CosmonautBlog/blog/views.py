# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def blog_create(request):
    return HttpResponse("<h1>Create</h1>")


def blog_detail(request):

    context = {
        "title": "Detail"
    }
    return render(request, "index.html", context)
    # return HttpResponse("<h1>Detail</h1>")


def blog_list(request):
    context = {
        "title": "List"
    }
    # if request.user.is_authenticated():
    #     context = {
    #         "title": "List"
    #     }
    # else:
    #     context = {
    #         "title": "List2"
    #     }
    return render(request, "index.html", context)
    # return HttpResponse("<h1>List</h1>")


def post_update(request):
    return HttpResponse("<h1>Update</h1>")


def post_delete(request):
    return HttpResponse("<h1>Delete</h1>")
