import pytest
from helpers.config_helper import *


@pytest.fixture(scope="session")
def api_key():
    return get_api_key()