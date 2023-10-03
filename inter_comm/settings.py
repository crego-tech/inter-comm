# -*- coding: utf-8 -*-
from dataclasses import dataclass

from django.conf import settings

# pylint: disable=invalid-name

_app_settings = getattr(settings, "INTER_COMM_SETTINGS", {})


@dataclass
class app_settings:
    """
    InterComm settings.
    """

    app_logger = _app_settings.get("app_logger")

    service_env = _app_settings.get("service_env", "local")

    config_secret = _app_settings.get("config_secret", {})
