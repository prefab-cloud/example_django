from django.urls import path

from . import views

app_name = "prefab"
urlpatterns = [
    path("", views.index, name="index"),
    path("<str:prefab_key>/", views.show, name="show")
]
