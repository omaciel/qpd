import datetime
from app.db import db
from flask_security import UserMixin, RoleMixin
from flask_security.utils import encrypt_password


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


class Project(db.Model):
    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), index=True, unique=True)

    def __repr__(self):
        return '<Project {0}>'.format(self.name)


class Release(db.Model):
    __tablename__ = 'releases'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), index=True, unique=True)
    major = db.Column(db.Integer, index=True)
    minor = db.Column(db.Integer, index=True)
    patch = db.Column(db.Integer, index=True)

    def __repr__(self):
        return '<Release {0}.{1}.{2}>'.format(
            self.major, self.minor, self.patch)

    def update_name(self):
        self.name = "{0}.{1}.{2}".format(
            self.major, self.minor, self.patch)


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
    timestamp = db.Column(db.DateTime, default=datetime.date.today())
    waved = db.Column(db.Boolean)
    operatingsystem_id = db.Column(
        db.Integer, db.ForeignKey('operatingsystems.id'))
    operatingsystem = db.relationship(
        'OperatingSystem',
        backref=db.backref('testruns', lazy='dynamic'),
    )
    project_id = db.Column(
        db.Integer, db.ForeignKey('projects.id'))
    project = db.relationship(
        'Project',
        backref=db.backref('testruns', lazy='dynamic'),
    )
    release_id = db.Column(
        db.Integer, db.ForeignKey('releases.id'))
    release = db.relationship(
        'Release',
        backref=db.backref('testruns', lazy='dynamic'),
    )

    passed = db.Column(db.Integer)
    failed = db.Column(db.Integer)
    skipped = db.Column(db.Integer)
    error = db.Column(db.Integer)
    total = db.Column(db.Integer)
    total_executed = db.Column(db.Integer)
    percent_passed = db.Column(db.Float)
    percent_failed = db.Column(db.Float)
    percent_executed = db.Column(db.Float)
    percent_not_executed = db.Column(db.Float)
    notes = db.Column(db.Text)

    def update_stats(self):
        self.total = sum([self.passed, self.failed, self.skipped, self.error])
        self.total_executed = sum([self.passed, self.failed])
        self.percent_passed = (
            (self.passed / float(self.total_executed)) * 100
            if self.total_executed > 0
            else 0)
        self.percent_failed = (
            (self.failed / float(self.total_executed)) * 100
            if self.total_executed > 0
            else 0)
        self.percent_executed = (
            (self.total_executed / float(self.total)) * 100
            if self.total > 0
            else 0)
        self.percent_not_executed = (
            (self.skipped / float(self.total)) * 100 if self.total > 0 else 0)


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

    def __repr__(self):
        return '<Operating System {0} {1}.{2}>'.format(
            self.name,
            self.major_version,
            self.minor_version,
        )

    def fullname(self):
        return '{0} {1}.{2}'.format(
            self.name,
            self.major_version,
            self.minor_version,
        )


# Define security models
roles_users = db.Table(
    'roles_users',
    db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
    db.Column('role_id', db.Integer(), db.ForeignKey('role.id'))
)


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

    def __str__(self):
        return self.name


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))

    def __str__(self):
        return self.email

    def set_password(self, password):
        self.password = encrypt_password(password)
