## Running the demo app

### Configure env

add a `.env` file with contents like

```
PREFAB_API_KEY="your key here"
PREFAB_API_URL="https://api.staging-prefab.cloud"
PREFAB_GRPC_URL="grpc.staging-prefab.cloud:443"
PREFAB_LOG_CLIENT_BOOTSTRAP_LEVEL=DEBUG
```
### Install requirements

Run
```
python -m pip install -r requirements.txt
```

This should install
* `Django`
* `django-environ` (for being able to load the .env file)
* `prefab_cloud_python` (from Github + its dependencies)

### Run the server

Run
```
python manage.py runserver
```

### Test it out

In your Prefab config, create values for `features.feature-1`, `config.config-1` with some lookup-key related rules

Navigate to

* `localhost:8000/prefab`
* `localhost:8000/prefab/features.feature-1`
* `localhost:8000/prefab/config.config-1`

Confirm that you are seeing the correct values!
