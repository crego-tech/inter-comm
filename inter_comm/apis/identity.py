# -*- coding: utf-8 -*-

import requests

from inter_comm.utils import get_host, handle_response


class IdentityAPIs:
    def __init__(self) -> None:
        self.app_name = "identity"
        self.root_host = get_host(self.app_name)

    def get_bulk_users(self, data):
        url = f"{self.root_host}/v1/{self.app_name}/users/bulk/internal/"
        response = requests.put(url, json=data, timeout=10)
        return handle_response(url, "PUT", {}, {}, response, self.app_name)

    def get_bulk_roles(self, data):
        url = f"{self.root_host}/v1/{self.app_name}/roles/bulk/internal/"
        response = requests.put(url, json=data, timeout=20)
        return handle_response(url, "PUT", data, {}, response, self.app_name)
