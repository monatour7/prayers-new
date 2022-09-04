import django.contrib.admin.sites
from django.urls import path, include
from rest_framework import routers

import prayers.prayersapp.views
from prayers.prayersapp import views


urlpatterns = [
   path('', prayers.prayersapp.views.index),
   path('l', django.contrib.admin.site.urls),
]