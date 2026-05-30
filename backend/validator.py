VALID_TYPES = [
    "form",
    "table",
    "dashboard",
    "card"
]

def validate_config(config):

    errors = []

    if "app_name" not in config:
        errors.append("Missing app_name")

    if "domain" not in config:
        errors.append("Missing domain")

    if "navigation" not in config:
        errors.append("Missing navigation")

    if "pages" not in config:
        errors.append("Missing pages")

    if "roles" not in config:
        errors.append("Missing roles")

    if "database_tables" not in config:
        errors.append("Missing database_tables")

    if "api_endpoints" not in config:
        errors.append("Missing api_endpoints")

    for page in config.get("pages", []):

        if "name" not in page:
            errors.append("Page missing name")

        if "type" not in page:
            errors.append("Page missing type")

        if page.get("type") not in VALID_TYPES:
            errors.append(
                f"Invalid page type: {page.get('type')}"
            )

        if page.get("type") == "form":

            if not page.get("fields"):
                errors.append(
                    f"{page['name']} form has no fields"
                )

        if page.get("type") == "table":

            if not page.get("columns"):
                errors.append(
                    f"{page['name']} table has no columns"
                )

        if page.get("type") == "dashboard":

            if not page.get("widgets"):
                errors.append(
                    f"{page['name']} dashboard has no widgets"
                )

        if page.get("type") == "card":

            if not page.get("widgets"):
                errors.append(
                    f"{page['name']} card has no widgets"
                )

    return errors