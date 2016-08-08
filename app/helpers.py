from app.models import OperatingSystem, TestRun


def operating_systems():
    """Returns a list of all existing operating systems."""
    return OperatingSystem.query.group_by(
        OperatingSystem.name,
        OperatingSystem.major_version,
    ).order_by(
        OperatingSystem.major_version.desc(),
    ).all()


def get_test_runs(operating_system=None, waved=False, items=10):
    """Returns a list of `Test Runs` for a given `OperatingSystem`."""
    runs = TestRun.query.filter_by(
        waved=waved).join(
            OperatingSystem).filter().order_by(
                TestRun.timestamp.desc(),
                TestRun.name.desc(),
                OperatingSystem.major_version.desc()
            )

    if operating_system:
        runs = runs.filter_by(operatingsystem=operating_system)

    return runs.limit(items)
