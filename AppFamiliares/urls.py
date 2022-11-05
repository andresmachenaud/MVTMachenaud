from django.urls import path
from AppFamiliares.views import *

urlpatterns = [
    path("", vista_familiares),
]
