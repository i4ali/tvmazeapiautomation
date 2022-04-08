import logging
import os

class TestNameFilter(logging.Filter):
    def filter(self, record):
        test_name = os.environ.get('PYTEST_CURRENT_TEST', "")
        if len(test_name) == 0:
            test_name = 'N/A'
        record.test_name = test_name
        return True


def get_custom_logger():
    logger = logging.getLogger(__name__)
    formatter = logging.Formatter('%(asctime)s - %(test_name)s - %(levelname)s: %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S%p')
    logger.setLevel(logging.DEBUG)
    fileHandler = logging.FileHandler('tvmaze-api.log', mode='a')
    fileHandler.setLevel(logging.DEBUG)
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)
    logger.addFilter(TestNameFilter())
    return logger