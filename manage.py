#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import click
from app import create_app, models, views, admin
from app.db import db
from app.helpers import create_user

app = create_app()

if app.config.get("LOGGER_ENABLED"):
    logging.basicConfig(
        level=getattr(logging, app.config.get("LOGGER_LEVEL", "DEBUG")),
        format=app.config.get(
            "LOGGER_FORMAT",
            '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'),
        datefmt=app.config.get("LOGGER_DATE_FORMAT", '%d.%m %H:%M:%S')
    )


@click.group()
def core_cmd():
    """ Core commands wrapper """
    pass


@core_cmd.command()
@click.option('--ipython/--no-ipython', default=True)
def shell(ipython):
    """Runs a Python shell with QPD context"""
    import code
    import readline
    import rlcompleter
    banner_msg = (
        "Welcome to QPD interactive shell\n"
        "\tAuto imported: app, db, models, views, admin"
    )
    _vars = globals()
    _vars.update(locals())
    _vars.update(dict(app=app, db=db, models=models, views=views, admin=admin))
    readline.set_completer(rlcompleter.Completer(_vars).complete)
    readline.parse_and_bind("tab: complete")
    try:
        if ipython is True:
            from IPython import start_ipython
            from traitlets.config import Config
            c = Config()
            c.TerminalInteractiveShell.banner2 = banner_msg
            start_ipython(argv=[], user_ns=_vars, config=c)
        else:
            raise ImportError
    except ImportError:
        shell = code.InteractiveConsole(_vars)
        shell.interact(banner=banner_msg)


@core_cmd.command()
def check():
    """Prints app status"""
    from pprint import pprint
    print("Extensions.")
    pprint(app.extensions)
    print("Modules.")
    pprint(app.blueprints)
    print("App.")
    return app


@core_cmd.command()
def showconfig():
    """Print all config variables"""
    from pprint import pprint
    print("Config.")
    pprint(dict(app.config))


@core_cmd.command()
@click.option('--reloader/--no-reloader', default=True)
@click.option('--debug/--no-debug', default=True)
@click.option('--host', default='127.0.0.1')
@click.option('--port', default=5000)
def run(reloader, debug, host, port):
    """Run the Flask development server i.e. app.run()"""
    app.run(use_reloader=reloader, debug=debug, host=host, port=port)


@core_cmd.command()
@click.option('--name', help='Full name', prompt=True)
@click.option('--email', help='A valid email address', prompt=True)
@click.option('--password', prompt=True, hide_input=True,
              confirmation_prompt=True)
def createsuperuser(name, email, password):
    """Create a user with administrator permissions"""
    create_user(name, email, password, 'admin', app=app)


help_text = """
    QPD Interactive shell!
    """
manager = click.CommandCollection(help=help_text)
manager.add_source(core_cmd)

if __name__ == '__main__':
    with app.app_context():
        manager()
