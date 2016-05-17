from . import db

import datetime


class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), index=True, unique=True)

    def __repr__(self):
        return '<Category {0}>'.format(self.name)


class Issue(db.Model):
    __tablename__ = 'issues'

    id = db.Column(db.Integer, primary_key=True)
    tracker_id = db.Column(db.Integer, db.ForeignKey('testtrackers.id'))
    tracker = db.relationship(
        'TestTracker',
        backref=db.backref('testtrackers', lazy='dynamic'),
    )
    number = db.Column(db.String(30), index=True)

    def __repr__(self):
        return '<Issue {0}>'.format(self.number)


class TestCase(db.Model):
    __tablename__ = 'testcases'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), index=True, unique=True)
    type_id = db.Column(db.Integer, db.ForeignKey('testtypes.id'))
    type = db.relationship(
        'TestType',
        backref=db.backref('testcases', lazy='dynamic'),
    )
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    category = db.relationship(
        'Category',
        backref=db.backref('testcases', lazy='dynamic'),
    )

    def __repr__(self):
        return '<Test Case {0}>'.format(self.name)


class TestRun(db.Model):
    __tablename__ = 'testruns'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), index=True)
    timestamp = db.Column(db.DateTime)
    waved = db.Column(db.Boolean)
    operatingsystem_id = db.Column(
        db.Integer, db.ForeignKey('operatingsystems.id'))
    operatingsystem = db.relationship(
        'OperatingSystem',
        backref=db.backref('operatingsystems', lazy='dynamic'),
    )
    passed = db.Column(db.Integer)
    failed = db.Column(db.Integer)
    skipped = db.Column(db.Integer)
    error = db.Column(db.Integer)
    total = db.Column(db.Integer)
    total_executed = db.Column(db.Integer)
    percent_passed = db.Column(db.Integer)
    percent_failed = db.Column(db.Integer)
    percent_executed = db.Column(db.Integer)
    percent_not_executed = db.Column(db.Integer)

    def __init__(
            self, passed, failed, skipped, error, operatingsystem_id,
            name=None, timestamp=None, waved=None):
        self.name = name or datetime.datetime.now().strftime(
            '%Y-%m-%d %H:%M:%S')
        self.passed = passed
        self.failed = failed
        self.skipped = skipped
        self.error = error

        if OperatingSystem.query.filter_by(
                id=operatingsystem_id).first() is not None:
            self.operatingsystem_id = operatingsystem_id

        self.timestamp = timestamp or datetime.datetime.now()
        if waved is None:
            self.waved = False

        self.total = sum([self.passed, self.failed, self.skipped, self.error])
        self.total_executed = sum([self.passed, self.failed])
        self.percent_passed = (
            (self.passed / self.total_executed) * 100
            if self.total_executed > 0
            else 0
        )
        self.percent_failed = (
            (self.failed / self.total_executed) * 100
            if self.total_executed > 0
            else 0)
        self.percent_executed = (
            (self.total_executed / self.total) * 100 if self.total > 0 else 0)
        self.percent_not_executed = (
            (self.skipped / self.total) * 100 if self.total > 0 else 0)


class TestType(db.Model):
    __tablename__ = 'testtypes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), index=True, unique=True)

    def __repr__(self):
        return '<Test Type {0}>'.format(self.name)


class TestResult(db.Model):
    __tablename__ = 'testresults'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), index=True, unique=True)

    def __repr__(self):
        return '<Test Result {0}>'.format(self.name)


class TestTracker(db.Model):
    __tablename__ = 'testtrackers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), index=True, unique=True)
    url = db.Column(db.String(255), unique=True)

    def __repr__(self):
        return '<Test Tracker {0}>'.format(self.name)


class OperatingSystem(db.Model):
    __tablename__ = 'operatingsystems'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), index=True)
    major_version = db.Column(db.Integer)
    minor_version = db.Column(db.Integer)

    def __init__(self, name, major=None, minor=None):
        self.name = name
        self.major_version = major or 0
        self.minor_version = minor or 0

    def __repr__(self):
        return '<Operating System {0} {1}.{2}>'.format(
            self.name,
            self.major_version,
            self.minor_version,
        )
