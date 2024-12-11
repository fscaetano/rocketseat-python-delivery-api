from pytest import raises
from .registry_order_validator import registry_order_validator


def test_registry_order_validator():
    body = {
        "data": {
            "name": "fulano",
            "address": "rua da paz, 123",
            "coupon": False,
            "items": [
                {"item": "soda", "quantity": 2},
                {"item": "pizza", "quantity": 3}
            ]
        }
    }
    registry_order_validator(body)


def test_registry_order_validator_with_errors():
    body = {
        "data": {
            "name": "fulano",
            "address": "rua da paz, 123",
            "coupon": "False",  # <--- should be boolean
            "items": [
                {"item": "soda", "quantity": 2},
                {"item": "pizza", "quantity": 3}
            ]
        }
    }

    with raises(Exception):
        registry_order_validator(body)
