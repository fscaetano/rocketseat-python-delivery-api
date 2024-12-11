from src.models.repository.interfaces.orders_repository import OrdersRepositoryInterface
from src.main.http_types.http_request import HttpRequest
from src.main.http_types.http_response import HttpResponse
from src.errors.error_handler import handle_errors
from src.errors.types.http_not_found import HttpNotFoundError


class RegistryFinder:
    def __init__(self, orders_repository: OrdersRepositoryInterface) -> None:
        self.__orders_repository = orders_repository

    def find(self, http_request: HttpRequest) -> HttpResponse:
        try:
            order_id = http_request.params["order_id"]

            order = self.search_order(order_id)

            return self.__format_response(order)
        except Exception as exception:
            return handle_errors(exception)

    def search_order(self, order_id: str):
        order = self.__orders_repository.select_by_object_id(order_id)
        if not order:
            raise HttpNotFoundError("Order not found")
        return order

    def __format_response(self, order: dict) -> dict:
        return HttpResponse(
            body={
                "data": {
                    "type": "Order",
                    "count": 1,
                    "attributes": order
                }
            },
            status_code=200
        )
