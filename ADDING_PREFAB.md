# Adding Prefab to a Django application

## Install dependencies

Add

```python
prefab-cloud-python==0.5.0
```

to your requirements. If you want to use prefab in template tags, you'll also need to add

```python
prefab-cloud-django==0.2.0
```

## Configure Prefab

In your `settings.py`

```
import prefab_cloud_python as prefab

options = prefab.Options(
    api_key=YOUR_PREFAB_API_KEY,
    ...
)

PREFAB = prefab.Client(options)
LOGGER = PREFAB.logger
```

## Using Prefab

Then, in your source files, you can use Prefab following its [documentation](https://docs.prefab.cloud/docs/python-sdk/python)

```
from django.conf import settings

def your_method(...):
    value = settings.PREFAB.get("your-config", default="whatever")
    settings.LOGGER.info(f"got {value} for 'your-config'")
```


## Using Prefab template tags

In your `views.py`

```
from prefab_cloud_python import Context

def index(request):
    context = Context({"user": {"name": "michael", "role": "developer"}})
    return render(request, "prefab/index.html", {"context": context})
```

In `templates/index.html`

```python
{% load prefab_tags %}

{% prefab_get "your-config" default="whatever" %}

{% prefab_enabled "your-feature-flag" context=context %}
```
