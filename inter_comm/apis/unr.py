# -*- coding: utf-8 -*-

import requests

from inter_comm.utils import get_host, handle_response


class UnRAPIs:
    def __init__(self) -> None:
        self.app_name = "unr"
        self.root_host = get_host(self.app_name)

    def get_bulk_banks(self, data):
        url = f"{self.root_host}/v1/{self.app_name}/banks/bulk/internal/"
        response = requests.put(url, json=data, timeout=10)
        return handle_response(url, "PUT", {}, {}, response, self.app_name)

    def get_bulk_programs(self, data):
        url = f"{self.root_host}/v1/{self.app_name}/programs/bulk/internal/"
        response = requests.put(url, json=data, timeout=20)
        return handle_response(url, "PUT", data, {}, response, self.app_name)

    def get_bulk_companies(self, data):
        url = f"{self.root_host}/v1/{self.app_name}/companies/bulk/internal/"
        response = requests.put(url, json=data, timeout=20)
        return handle_response(url, "PUT", data, {}, response, self.app_name)
