# -*- coding: utf-8 -*-

from inter_comm.settings import app_settings

# pylint: disable=broad-exception-raised


def handle_response(url, method, payload, headers, response, service_name):  # pylint: disable=too-many-arguments
    app_settings.app_logger.info(
        {
            "url": url,
            "method": method,
            "request": payload,
            "response": response.text,
            "status_code": response.status_code,
            "headers": headers,
        }
    )
    if response.status_code in range(200, 300):
        return response.json()
    if response.status_code in range(400, 499):
        raise Exception(response.json())
    raise Exception(
        {
            "message": f"Something went wrong with {service_name.title()} service",
            "description": response.text,
        },
        response.status_code,
    )


def get_host(service_name):
    if app_settings.service_env != "local":
        root_host = f"http://{service_name}.{app_settings.config_secret.get('service_discovery')}"
    else:
        root_host = app_settings.config_secret.get("internal_service_host")
    return root_host


def filter_queryset(queryset, auth_data, is_root):
    if auth_data.get("lead_id"):
        if is_root:
            queryset = queryset.filter(lead_id=auth_data["lead_id"])
        else:
            queryset = queryset.filter(account__lead_id=auth_data["lead_id"])
    elif auth_data.get("program_id"):
        if is_root:
            queryset = queryset.filter(program_id=auth_data["program_id"])
        else:
            queryset = queryset.filter(account__program_id=auth_data["program_id"])
    elif auth_data.get("company_id"):
        from inter_comm.apis.unr import UnRAPIs  # pylint: disable=import-outside-toplevel

        companies = UnRAPIs().get_bulk_companies({"ids": [auth_data["company_id"]], "type": ["all_programs"]})
        if companies:
            program_ids = [program["id"] for program in companies[0].get("all_programs", [])]
        else:
            program_ids = []
        if is_root:
            queryset = queryset.filter(program_id__in=program_ids)
        else:
            queryset = queryset.filter(account__program_id__in=program_ids)
    return queryset
