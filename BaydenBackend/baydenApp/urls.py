from django.urls import path
from .views import homepage, index

urlpatterns = [
    path("test/", homepage, name="homepage"),
    path("", index, name="index")
]