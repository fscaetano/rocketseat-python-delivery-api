from src.main.http_types.http_response import HttpResponse
from .types.http_unauthorized import HttpUnauthorizedError
from .types.http_bad_request import HttpBadRequestError
from .types.http_not_found import HttpNotFoundError
from .types.http_unprocessable_entity import HttpUnprocessableEntityError

def handle_errors(error: Exception) -> HttpResponse:
    if isinstance(error, (HttpUnauthorizedError, HttpBadRequestError, HttpNotFoundError, HttpUnprocessableEntityError)):
        return HttpResponse(
            body={
                "errors": [{
                    "title": error.name,
                    "detail": error.message
                }]
            },
            status_code=error.status_code
        )

    return HttpResponse(
        body={
            "errors": [{
                "title": "Server Error",
                "detail": str(error)
            }]
        },
        status_code=500)
