from app.db import db
from app.models import OperatingSystem, Release, TestRun, Role, User
from sqlalchemy.sql.functions import func

import datetime
import json


def operating_systems():
    """Returns a list of all existing operating systems."""
    return OperatingSystem.query.group_by(
        OperatingSystem.name,
        OperatingSystem.major_version,
    ).order_by(
        OperatingSystem.major_version.desc(),
    ).all()


def format_for_table(items, fields, reverse=True):

    data = []

    for item in items:
        row = []
        for field in fields:
            value = getattr(item, field, 0)
            if type(value) == datetime.datetime:
                value = value.strftime('%Y-%m-%d')
            row.append(value)
        data.append(row)
    if reverse:
        data.reverse()
    return json.dumps(data)


def get_average_test_runs(items=None, release=None):
    """Returns a list of `Test Runs` grouped by a `Release`."""
    avg_runs = db.session.query(
        TestRun.name,
        func.avg(TestRun.passed).label('passed'),
        func.avg(TestRun.failed).label('failed'),
        func.avg(TestRun.skipped).label('skipped'),
        func.avg(TestRun.error).label('error'),
        func.avg(TestRun.percent_passed).label('percent_passed'),
        func.avg(TestRun.percent_failed).label('percent_failed'),
        func.avg(TestRun.percent_executed).label('percent_executed'),
        func.avg(TestRun.percent_not_executed).label('percent_not_executed'),
    ).group_by(
        TestRun.release_id,
        TestRun.name
    ).order_by(
            TestRun.timestamp.desc(),
            TestRun.name.desc(),
        )

    avg_runs = avg_runs.filter_by(
            waved=False
        )

    if release:
        avg_runs = avg_runs.filter_by(release=release)

    if items:
        avg_runs = avg_runs.limit(items)

    return avg_runs


def get_latest_test_runs():
    testruns = []

    # All releases
    releases = Release.query.order_by(Release.name.desc()).all()

    for release in releases:
        # Fetch unique operating systems tested in a release
        oses = set(
            testrun.operatingsystem
            for testrun
            in TestRun.query.filter_by(release=release).all())
        # Get latest test run result for each operating system
        for operatingsystem in oses:
            testruns.append(
                TestRun.query.filter_by(
                    release=release,
                    operatingsystem=operatingsystem
                ).order_by(
                    TestRun.timestamp.desc()
                ).first())

    return testruns


def get_test_runs(items=None, op_system=None, release=None, waved=False):
    """Returns a list of `Test Runs` for a given `OperatingSystem`."""
    runs = TestRun.query.filter_by(
        waved=waved)

    if op_system:
        runs = runs.filter_by(operatingsystem=op_system)

    if release:
        runs = runs.filter_by(release=release)

    runs = runs.join(
            OperatingSystem, Release).filter().order_by(
                TestRun.timestamp.desc(),
                TestRun.name.desc(),
                Release.name.desc(),
                OperatingSystem.major_version.desc()
            )

    if items:
        runs = runs.limit(items)

    return runs


def get_or_create(model, **kwargs):
    """SQLAlchemy helper to get_or_create an object"""
    instance = db.session.query(model).filter_by(**kwargs).first()
    if instance:
        return instance, False
    else:
        instance = model(**kwargs)
        db.session.add(instance)
        return instance, True


def create_user(
        name=None, email=None,
        password=None, role=None, app=None):
    "Create a user"

    role, created = get_or_create(Role, name=role)

    with app.app_context():
        if all([name, email, password]):
            user = User(
                first_name=name,
                roles=[role],
                active=True,
                email=email
            )
            user.set_password(password)
            db.session.add(user)
        else:
            user = "Cant create the user"
        db.session.commit()
        print(user)
