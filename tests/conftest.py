import time
import pytest
from utilities import customlogger

logger = customlogger.get_custom_logger()


@pytest.yield_fixture(name="time_request")
def fix_time_request():
    t0 = time.time()
    yield
    t1 = time.time()
    logger.debug("Test took %s seconds", t1-t0)


