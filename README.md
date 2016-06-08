# Quality Product Data #

Dashboard to capture and display automation results generated from
[Robottelo](https://github.com/SatelliteQE/robottelo).


![Dashboard](https://omaciel.fedorapeople.org/dashboard.png)


## Usage ##

```bash
$ python manage.py
Usage: manage.py [OPTIONS] COMMAND [ARGS]...

      QPD Interactive shell!

Options:
  --help  Show this message and exit.

Commands:
  check       Prints app status
  run         Run the Flask development server i.e.
  shell       Runs a Python shell with QPD context
  showconfig  Print all config variables
```

to run the application


```bash
$ python manage.py run
08.06 16:07:28 werkzeug     INFO      * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
08.06 16:07:28 werkzeug     INFO      * Restarting with stat
08.06 16:07:28 werkzeug     WARNING   * Debugger is active!
08.06 16:07:28 werkzeug     INFO      * Debugger pin code: 223-716-766
```


to specify a *port* and other attributes handled by *werkzeug*


```bash
$ python manage.py run --port=9000 --host=127.0.0.1 --debug --reloader
08.06 10:49:41 werkzeug     INFO      * Running on http://127.0.0.1:9000/ (Press CTRL+C to quit)
08.06 10:49:41 werkzeug     INFO      * Restarting with stat
08.06 10:49:41 werkzeug     WARNING   * Debugger is active!
08.06 10:49:41 werkzeug     INFO      * Debugger pin code: 121-731-875
```


to start the shell


```bash
$ python manage.py shell
Python 2.7.11 (default, Mar 31 2016, 20:46:51)
Welcome to QPD interactive shell
	Auto imported: app, db, models, views, admin
In [1]: app
Out[1]: <Flask 'app'>

In [2]: models.Category.query.all()
Out[2]: [<Category cli>]
```
