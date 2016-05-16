from flask import render_template, redirect, url_for, request
from ..models import TestRun
from . import main


@main.route('/')
def index():
    test_runs = TestRun.query.all()
    return render_template('index.html', runs=test_runs)
