
from django.urls import path
from .views import show_task
from tasks.views import abtahi,show_specific_task
urlpatterns = [
    path("show/",show_task)
    path("Showtesks/<id>",show_specific_task)
]