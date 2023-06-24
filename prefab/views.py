from django.shortcuts import render

from django.conf import settings

from prefab_cloud_python import Context


def index(request):
    settings.LOGGER.debug("SHOWN: debug")
    settings.LOGGER.info("SHOWN: info")
    settings.LOGGER.warn("SHOWN: warn")
    settings.LOGGER.error("SHOWN: error")
    settings.LOGGER.critical("SHOWN: critical")
    context = Context({"michael": {"is_michael": True}})
    return render(request, "prefab/index.html", {"prefab": settings.PREFAB, "context": context})


def show(request, prefab_key):
    settings.LOGGER.debug("HIDDEN: debug")
    settings.LOGGER.info("HIDDEN: info")
    settings.LOGGER.warn("SHOWN: warn")
    settings.LOGGER.error("SHOWN: error")
    settings.LOGGER.critical("SHOWN: critical")
    settings.LOGGER.error(request.GET)
    lookup_key = request.GET.get("lookup_key")
    default = request.GET.get("default")
    return render(request, "prefab/show.html", {"key": prefab_key, "lookup_key": lookup_key, "default": default, "properties": {}})
