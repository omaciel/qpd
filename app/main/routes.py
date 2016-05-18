from flask import render_template, redirect, url_for, request
from ..models import OperatingSystem, TestRun
from . import main


@main.route('/')
def index():
    test_runs = TestRun.query.join(
        OperatingSystem).filter().order_by(
            TestRun.timestamp.desc(), OperatingSystem.major_version.desc())
    return render_template('index.html', runs=test_runs)
