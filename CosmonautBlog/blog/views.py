# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post


def blog_create(request):
    return HttpResponse("<h1>Create</h1>")


def blog_detail(request, id=None):
    instance = get_object_or_404(Post, id=id)
    context = {
        "title": instance.title,
        "instance": instance
    }
    return render(request, "post_detail.html", context)
    # return HttpResponse("<h1>Detail</h1>")


def blog_list(request):
    queryset = Post.objects.all()
    context = {
        "objects_list": queryset,
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
