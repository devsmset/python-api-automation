""" This is a test script for API testing"""

import requests
import pytest
from pydantic import ValidationError
from requests.exceptions import RequestException
from models.user import User
from helpers.log_helper import logger
from helpers.config_helper import get_url



def test_get_users():
    """ Gets a list of users"""
    response = requests.get(get_url("public/v2/users"), timeout=180)
    assert response.status_code == 200
    for item in response.json():
        try:
            user = User(**item)
            logger.info("Model validated with name %s", user.name)
        except ValidationError:
            assert False


@pytest.mark.parametrize("per_page, page", [(10, 1), (10, 2), (5, 8)])
@pytest.mark.paginate
def test_paginate_user(per_page, page):
    """ Gets paginated user list"""
    response = requests.get(
        get_url("public/v2/users"),
        params={'per_page': per_page, 'page': page},
        timeout=180
    )
    logger.info(response.json())


@pytest.mark.fail
def test_post_user(api_key):
    """ Creates user """
    headers = {'Authorization': f'Bearer {api_key}'}
    user = User(
        id=10119099,
        name="Amit Karmakar",
        email="amit3@example.com",
        gender="male",
        status="active"
    )
    try:
        response = requests.post(
            url=get_url("public/v2/users"),
            headers=headers,
            data=user.model_dump(),
            timeout=180
        )
        response.raise_for_status()
    except RequestException as e:
        logger.error("Exception occurred: %s", e)
        assert False
    assert response.json() != ''
