from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'chefBot.views.home', name='home'),
    url(r'^myFridge/', include('myFridge.urls')),
    url(r'^admin/', admin.site.urls),
]
