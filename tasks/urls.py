
from django.urls import path
from .views import show_task
from tasks.views import abtahi
urlpatterns = [
    path("show/",show_task),
    path("abtahi/",abtahi),
]