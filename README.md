# emenu
Portfolio service with API for restaurants' menus

## How to install

Pull repository. Go to `emenu/emenu` dir, where `settings.py` exists. Create file
`secret_key.txt` and paste Django's `SECRET_KEY` inside.

## Todo
1. Split settings so that we can run django locally without docker.
To do that modify asgi.py and point to settings_dev