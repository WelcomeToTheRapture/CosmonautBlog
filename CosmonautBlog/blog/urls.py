from django.conf.urls import url
from .views import (blog_create, blog_detail,
                    blog_list, post_update,
                    post_delete)

urlpatterns = [
    url(r'^$', blog_list),
    url(r'^create/$', blog_create),
    url(r'^detail/$', blog_detail),
    url(r'^update/$', post_update),
    url(r'^delete/$', post_delete),
]
