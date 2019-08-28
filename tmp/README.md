## Run

#### Desc

Client => WebServer => APServer => DBServer


#### Use python

```
$ python run.py
```

#### Use uWSGI

```
$ uwsgi --http=0.0.0.0:8080 --wsgi-file=run.py  --callable=app

or

$ uwsgi uwsgi.ini
```

#### Reload

```
$ uwsgi --reload /var/run/uwsgi/uwsgi.pid
```

#### Stop

```
$ uwsgi --stop /var/run/uwsgi/uwsgi.pid
```
