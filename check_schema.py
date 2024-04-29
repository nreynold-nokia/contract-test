import json

from fastapi.openapi.utils import get_openapi

from main import app


def create_openapi_json_file():
    with open("./temp-openapi.json", "w") as openapi_json_file:
        openapi_json_file.write(
            json.dumps(
                get_openapi_json(),
                indent=2,
            )
        )


def get_openapi_json():
    openapi_json = get_openapi(
        title=app.title,
        version=app.version,
        openapi_version=app.openapi_version,
        description=app.description,
        routes=app.routes,
    )
    return openapi_json


if __name__ == "__main__":
    create_openapi_json_file()
