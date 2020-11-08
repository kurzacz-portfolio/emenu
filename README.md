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
```shell script
$ docker-compose up
```


## Browse API
Create a user first, so you may authorize for secured API endpoints. Do this e.g.
with command `$ python manage.py createsuperuser`

Visit URL http://localhost:8000/swagger/. Authenticate with endpoint `auth`.
Then, copy token. Use button *Authorize* and paste token with prefix `Token `, e.g.:
`Token 1e2e563f36f2efe83d0f282da9205aa7eefcceed` 


## Running tests

Create virtual environment in main directory:
```shell script
$ python3 -m venv
```

Next, activate it:
```shell script
$ source venv/bin/activate
```

Then, install all requirements:
```shell script
$ pip install -U pip
$ pip install -r emenu/requirements.txt
$ pip install -r emenu/requirements.dev.txt
```

Before you run tests, you need working postgresql database. One way is to start
Docker Compose as described in previous section. After `docker-compose up`, run
following command to actually start tests:
```shell script
cd emenu
emenu$ ./manage.py test api/tests
```

For test coverage report, still in the `emenu` subfolder, run following commands:
```shell script
emenu$ coverage run --source='api' manage.py test api/tests
emenu$ coverage report
```