import pytest
import time


@pytest.yield_fixture
def setup():
    print("running setup")
    yield
    print("running teardown")


@pytest.yield_fixture(name="time_request")
def fix_time_request():
    t0 = time.time()

    yield

    t1 = time.time()

    print("Test took %s seconds", t1 - t0)