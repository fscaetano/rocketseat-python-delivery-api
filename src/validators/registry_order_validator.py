from cerberus import Validator


def registry_order_validator(body: any):
    body_validator = Validator({
        "data": {
            "type": "dict",
            "schema": {
                "name": {"type": "string", "required": True},
                "address": {"type": "string", "required": True},
                "coupon": {"type": "boolean", "required": True},
                "items": {
                    "type": "list",
                    "schema": {
                        "type": "dict",
                        "schema": {
                            "item": {"type": "string", "required": True},
                            "quantity": {"type": "integer", "required": True}
                        }
                    }
                }
            }
        }
    })

    response = body_validator.validate(body)
    if response is False:
        raise Exception(body_validator.errors)