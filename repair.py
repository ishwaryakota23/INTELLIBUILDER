VALID_TYPES = [
    "form",
    "table",
    "dashboard",
    "card"
]

def repair_config(config):

    repairs = []

    if "pages" not in config:

        config["pages"] = []

        repairs.append(
            "Added missing pages"
        )

    if "roles" not in config:

        config["roles"] = [
            "Admin"
        ]

        repairs.append(
            "Added default role"
        )

    if "database_tables" not in config:

        config["database_tables"] = []

        repairs.append(
            "Added database tables"
        )

    if "api_endpoints" not in config:

        config["api_endpoints"] = []

        repairs.append(
            "Added API endpoints"
        )

    for page in config.get(
        "pages",
        []
    ):

        if page.get("type") not in VALID_TYPES:

            page["type"] = "card"

            repairs.append(
                f"Fixed page type in {page['name']}"
            )

        if (
            page["type"] == "table"
            and
            not page.get("columns")
        ):

            page["columns"] = [
                "Name",
                "Status"
            ]

            repairs.append(
                f"Added columns to {page['name']}"
            )

        if (
            page["type"] == "form"
            and
            not page.get("fields")
        ):

            page["fields"] = [
                "Name"
            ]

            repairs.append(
                f"Added fields to {page['name']}"
            )
    if "permissions" not in config:
        config["permissions"] = {
            "Admin": [
                "Create",
                "Read",
                "Update",
                "Delete"
            ]
        }
        repairs.append(
        "Generated default permissions"
        )
    return config, repairs