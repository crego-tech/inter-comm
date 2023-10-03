# -*- coding: utf-8 -*-

import requests

from inter_comm.utils import get_host, handle_response


class CRMAPIs:
    def __init__(self) -> None:
        self.app_name = "crm"
        self.root_host = get_host(self.app_name)

    def get_bulk_leads(self, data):
        url = f"{self.root_host}/v1/{self.app_name}/leads/bulk/internal/"
        response = requests.put(url, json=data, timeout=10)
        return handle_response(url, "PUT", {}, {}, response, self.app_name)

    def check_line_amount(self, lead_id, data, headers):
        url = f"{self.root_host}/v1/{self.app_name}/leads/{lead_id}/check_line_amount/"
        response = requests.put(
            url=url,
            json=data,
            headers=headers,
            timeout=20,
        )
        return handle_response(url, "PUT", {"lead_id": lead_id, "data": data}, headers, response, self.app_name)

    def update_bulk_lead_details(self, data):
        url = f"{self.root_host}/v1/{self.app_name}/leads/bulk_update/"
        response = requests.patch(url=url, json=data, timeout=20)
        return handle_response(url, "PUT", data, {}, response, self.app_name)
