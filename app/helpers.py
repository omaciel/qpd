from app.models import OperatingSystem, TestRun


def operating_systems():
    """Returns a list of all existing operating systems."""
    return OperatingSystem.query.group_by(
        OperatingSystem.name,
        OperatingSystem.major_version,
    ).order_by(
        OperatingSystem.major_version.desc(),
    ).all()


def get_test_runs(items=None, op_system=None, release=None, waved=False):
    """Returns a list of `Test Runs` for a given `OperatingSystem`."""
    runs = TestRun.query.filter_by(
        waved=waved)

    if op_system:
        runs = runs.filter_by(operatingsystem=op_system)

    if release:
        runs = runs.filter_by(release=release)

    runs = runs.join(
            OperatingSystem).filter().order_by(
                TestRun.timestamp.desc(),
                TestRun.name.desc(),
                OperatingSystem.major_version.desc()
            )

    if items:
        runs = runs.limit(items)

    return runs
