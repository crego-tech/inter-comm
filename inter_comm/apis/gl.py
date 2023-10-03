# -*- coding: utf-8 -*-

import requests

from inter_comm.utils import get_host, handle_response


# pylint: disable=too-few-public-methods
class GLAPIs:
    def __init__(self) -> None:
        self.app_name = "gl"
        self.root_host = get_host(self.app_name)

    def create_account(self, data):
        url = f"{self.root_host}/v1/{self.app_name}/accounts/internal/"
        response = requests.post(url, json=data, timeout=10)
        return handle_response(url, "POST", {}, {}, response, self.app_name)
