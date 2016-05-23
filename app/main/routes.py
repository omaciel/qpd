from flask import render_template, redirect, url_for
from ..models import OperatingSystem, TestRun
from . import main


@main.route('/')
def index():
    test_runs = TestRun.query.join(
        OperatingSystem).filter().order_by(
            TestRun.timestamp.desc(), OperatingSystem.major_version.desc())
    return render_template('index.html', runs=test_runs)


@main.route('/operatingsystems/', methods=['GET', ])
def operatingsystems():
    oses = OperatingSystem.query.order_by(
        OperatingSystem.name.desc(), OperatingSystem.major_version.desc())
    return render_template('operatingsystems.html', oses=oses)


@main.route('/operatingsystems/<int:id>', methods=['GET', ])
def operatingsystem(id):
    operatingsystem = OperatingSystem.query.filter_by(id=id).first()
    if operatingsystem is None:
        return redirect(url_for('operatingsystems'))
    test_runs = TestRun.query.join(
        OperatingSystem).filter_by(id=operatingsystem.id).order_by(
            TestRun.timestamp.desc(), OperatingSystem.major_version.desc())

    return render_template(
        'operatingsystem.html',
        name='{0} {1}'.format(
            operatingsystem.name,
            operatingsystem.major_version,
        ),
        runs=test_runs
    )
