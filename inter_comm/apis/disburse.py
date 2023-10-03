# -*- coding: utf-8 -*-

import requests

from inter_comm.utils import get_host, handle_response


class DisburseAPIs:
    def __init__(self) -> None:
        self.app_name = "disburse"
        self.root_host = get_host(self.app_name)

    def get_bulk_accounts(self, data):
        url = f"{self.root_host}/v1/{self.app_name}/accounts/bulk/internal/"
        response = requests.put(url, json=data, timeout=10)
        return handle_response(url, "PUT", {}, {}, response, self.app_name)

    def get_bulk_topups(self, data):
        url = f"{self.root_host}/v1/{self.app_name}/topups/bulk/internal/"
        response = requests.put(url, json=data, timeout=10)
        return handle_response(url, "PUT", {}, {}, response, self.app_name)
