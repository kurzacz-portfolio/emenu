# emenu
Portfolio service with API for restaurants' menus.

Used main technologies:
* Python 3.7
* Django + Django Rest Framework
* Docker (with Compose)

## How to run

Pull repository. Go to `emenu/emenu` dir, where `settings.py` exists. Create file
`secret_key.txt` and paste Django's `SECRET_KEY` inside.

Start whole project with:
```
$ docker-compose up
```

## Todo
1. Split settings so that we can run django locally without docker.
To do that modify asgi.py and point to settings_dev