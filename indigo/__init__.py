TYPE_PROJECT_PUBLIC_ID = "project"
TYPE_ORGANISATION_PUBLIC_ID = "organisation"

JSONDATAFERRET_HOOKS = "indigo.jsondataferret"

TYPE_PROJECT_ALWAYS_FILTER_KEYS_LIST = ["/status"]
TYPE_PROJECT_FILTER_KEYS_LIST = ["/stage_development"]
TYPE_PROJECT_FILTER_LISTS_LIST = ["/outcome_funds"]

TYPE_PROJECT_ORGANISATION_REFERENCES_LIST = [
    {
        "list_key": "/service_provisions",
        "item_organisation_id_key": "/organisation_id/value",
    },
    {
        "list_key": "/outcome_payment_commitments",
        "item_organisation_id_key": "/organisation_id/value",
    },
    {"list_key": "/investments", "item_organisation_id_key": "/organisation_id/value"},
    {
        "list_key": "/intermediary_services",
        "item_organisation_id_key": "/organisation_id/value",
    },
    # TODO the comma separated orgs in Results tab
    # TODO the comma separated orgs in outcome funds tab
]

TYPE_PROJECT_ORGANISATION_LIST = {
    # The key in the whole project data where we look for the list
    "list_key": "/organisations",
    # In each item in the list, the key where we find the public ID of the organisation
    "item_id_key": "/id",
    # If the item in the list has other org fields that we should pull out of the org record, put them here
    # key is key in item in list: value is key in organisation record (this should always start with a slash )
    "item_to_org_map": {
        "/org-ids/company/value": "/org-ids/company/value",
        "/org-ids/charity/value": "/org-ids/charity/value",
        "/org-ids/other/value": "/org-ids/other/value",
        "/contact/name/value": "/contact/name/value",
        "/contact/email/value": "/contact/email/value",
        "/website/value": "/website/value",
        "/address/value": "/address/value",
        "/postcode/value": "/postcode/value",
        "/country/value": "/country/value",
    },
}

TYPE_PROJECT_SOURCE_LIST = {
    # The key in the whole project data where we look for the list
    "list_key": "/sources",
    # In each item in the list, the key where we find the ID of the source
    "item_id_key": "/id",
}
TYPE_PROJECT_SOURCES_REFERENCES_LIST = [
    {"list_key": "/intermediary_services", "item_source_ids_key": "/source_ids",}
    # TODO find and add the rest
]

TYPE_ORGANISATION_ALWAYS_FILTER_KEYS_LIST = ["/contact"]
