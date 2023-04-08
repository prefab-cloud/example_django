from django.shortcuts import render


def index(request):
    return render(request, "prefab/index.html")


def show(request, prefab_key):
    return render(request, "prefab/show.html", {"key": prefab_key})
