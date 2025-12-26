import os

import pytest


@pytest.mark.unit
class TestInitial:
    def test_env(self, settings):
        assert os.environ.get("ENV") == "test"

    def test_settings(self, settings):
        assert settings.ENV == "test"
        assert settings.DEBUG == True
        assert settings.BASE_URL == ""
